import { invoke } from "@tauri-apps/api/core"

export async function pickFolder(): Promise<string | null> {
  try {
    return await invoke<string | null>("pick_folder")
  } catch {
    return null
  }
}

export async function pickFile(): Promise<string | null> {
  try {
    return await invoke<string | null>("pick_file")
  } catch {
    return null
  }
}

export async function readFile(path: string): Promise<string> {
  return invoke<string>("read_file", { path })
}

export async function writeFile(path: string, content: string): Promise<void> {
  return invoke<void>("write_file", { path, content })
}

export async function openFolder(path: string): Promise<string[]> {
  return invoke<string[]>("open_folder", { path })
}

export async function getBackendStatus(): Promise<string> {
  return invoke<string>("get_backend_status")
}