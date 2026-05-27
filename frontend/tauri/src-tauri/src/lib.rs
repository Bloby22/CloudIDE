pub mod backend;
pub mod commands;

use backend::BackendSidecar;

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .plugin(tauri_plugin_fs::init())
        .plugin(tauri_plugin_dialog::init())
        .plugin(tauri_plugin_process::init())
        .plugin(tauri_plugin_window_state::Builder::default().build())
        .setup(|app| {
            let handle = app.handle().clone();
            tauri::async_runtime::spawn(async move {
                let sidecar = BackendSidecar::new(handle);
                sidecar.start().await;
            });
            Ok(())
        })
        .invoke_handler(tauri::generate_handler![
            commands::get_backend_status,
            commands::open_folder,
        ])
        .run(tauri::generate_context!())
        .expect("error while running CloudIDE");
}

.invoke_handler(tauri::generate_handler![
    commands::get_backend_status,
    commands::open_folder,
    commands::pick_folder,
    commands::pick_file,
    commands::read_file,
    commands::write_file,
])