#include <iostream>
#include <string>
#include <thread>
#include <chrono>
#include <filesystem>
#include <cstdlib>

#ifdef _WIN32
#include <windows.h>
#include <urlmon.h>
#pragma comment(lib, "urlmon.lib")
#else
#include <unistd.h>
#endif

namespace fs = std::filesystem;

static bool wait_for_backend(const std::string& url, int timeout_sec = 15) {
    auto start = std::chrono::steady_clock::now();
    while (true) {
#ifdef _WIN32
        HRESULT hr = URLDownloadToFileA(nullptr, (url + "/health").c_str(), "NUL", 0, nullptr);
        if (SUCCEEDED(hr)) return true;
#else
        int code = std::system(("curl -sf " + url + "/health > /dev/null 2>&1").c_str());
        if (code == 0) return true;
#endif
        auto elapsed = std::chrono::steady_clock::now() - start;
        if (std::chrono::duration_cast<std::chrono::seconds>(elapsed).count() >= timeout_sec)
            return false;
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
    }
}

static void start_backend(const std::string& root) {
    std::string python  = root + "\\.venv\\Scripts\\python.exe";
    std::string main_py = root + "\\backend\\src\\app\\main.py";

    if (!fs::exists(python)) python = "python";

#ifdef _WIN32
    std::string cmd = "start /B \"CloudIDE Backend\" \"" + python + "\" \"" + main_py + "\"";
    std::system(cmd.c_str());
#else
    std::string cmd = python + " " + main_py + " &";
    std::system(cmd.c_str());
#endif
}

static void start_frontend(const std::string& root) {
#ifdef _WIN32
    std::string exe = root + "\\build\\CloudIDE.exe";
    if (fs::exists(exe)) {
        ShellExecuteA(nullptr, "open", exe.c_str(), nullptr, nullptr, SW_SHOW);
    } else {
        std::string cmd = "start /B \"CloudIDE Frontend\" cmd /C \"cd " + root + "\\frontend && npm run dev\"";
        std::system(cmd.c_str());
        ShellExecuteA(nullptr, "open", "http://localhost:5173", nullptr, nullptr, SW_SHOW);
    }
#else
    std::string cmd = "cd " + root + "/frontend && npm run dev &";
    std::system(cmd.c_str());
#endif
}

int main(int argc, char* argv[]) {
    std::string root = fs::current_path().string();
    if (argc > 1) root = argv[1];

    std::cout << "[Bootstrap] CloudIDE starting...\n";
    std::cout << "[Bootstrap] Root: " << root << "\n";

    std::cout << "[Bootstrap] Starting backend...\n";
    start_backend(root);

    std::cout << "[Bootstrap] Waiting for API (localhost:8000)...\n";
    if (!wait_for_backend("http://localhost:8000")) {
        std::cerr << "[Bootstrap] ERROR: Backend failed to start within 15s\n";
        return 1;
    }
    std::cout << "[Bootstrap] API ready\n";

    std::cout << "[Bootstrap] Starting frontend...\n";
    start_frontend(root);

    std::cout << "[Bootstrap] CloudIDE running\n";

#ifdef _WIN32
    MSG msg;
    while (GetMessage(&msg, nullptr, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }
#else
    pause();
#endif

    return 0;
}
