use std::process::{Child, Command};
use std::path::PathBuf;
use std::time::Duration;
use tauri::AppHandle;
use tauri::Manager;

pub struct BackendSidecar {
    handle: AppHandle,
}

impl BackendSidecar {
    pub fn new(handle: AppHandle) -> Self {
        Self { handle }
    }

    fn backend_path(&self) -> PathBuf {
        let res = self.handle
            .path()
            .resource_dir()
            .unwrap_or_else(|_| PathBuf::from("."));

        #[cfg(debug_assertions)]
        {
            PathBuf::from("../backend/src/app/main.py")
        }
        #[cfg(not(debug_assertions))]
        {
            res.join("backend").join("src").join("app").join("main.py")
        }
    }

    fn python_path(&self) -> String {
        #[cfg(debug_assertions)]
        {
            let venv = PathBuf::from("../backend/.venv/Scripts/python.exe");
            if venv.exists() {
                return venv.to_string_lossy().to_string();
            }
        }
        "python".to_string()
    }

    pub async fn start(&self) {
        let python = self.python_path();
        let script = self.backend_path();

        println!("[Sidecar] Starting backend: {} {}", python, script.display());

        let mut child: Option<Child> = Command::new(&python)
            .arg(&script)
            .spawn()
            .map_err(|e| eprintln!("[Sidecar] Failed to start backend: {}", e))
            .ok();

        self.wait_for_ready().await;
        println!("[Sidecar] Backend ready on :8000");

        if let Some(ref mut c) = child {
            let _ = c.wait();
        }
    }

    async fn wait_for_ready(&self) {
        let client = reqwest::Client::new();
        for _ in 0..30 {
            tokio::time::sleep(Duration::from_millis(500)).await;
            if client
                .get("http://localhost:8000/health")
                .send()
                .await
                .is_ok()
            {
                return;
            }
        }
        eprintln!("[Sidecar] Backend did not start in time");
    }
}
