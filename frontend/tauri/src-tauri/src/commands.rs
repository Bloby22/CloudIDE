use tauri::command;

#[command]
pub async fn get_backend_status() -> Result<String, String> {
    let client = reqwest::Client::new();
    match client
        .get("http://localhost:8000/health")
        .send()
        .await
    {
        Ok(r) => {
            let json: serde_json::Value = r.json().await.unwrap_or_default();
            Ok(json.to_string())
        }
        Err(e) => Err(format!("Backend unreachable: {}", e)),
    }
}

#[command]
pub async fn open_folder(path: String) -> Result<Vec<String>, String> {
    let entries = std::fs::read_dir(&path)
        .map_err(|e| e.to_string())?
        .filter_map(|e| e.ok())
        .map(|e| e.path().to_string_lossy().to_string())
        .collect();
    Ok(entries)
}
