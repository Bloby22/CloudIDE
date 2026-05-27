#include <iostream>
#include <cstdlib>
#include <filesystem>

namespace fs = std::filesystem;

int main(int argc, char* argv[]) {
    std::string root = fs::current_path().string();
    if (argc > 1) root = argv[1];
    std::cout << "[Launcher] Starting CloudIDE from: " << root << "\n";
    std::string bootstrap = root + "\\Bootstrap.exe";
    if (fs::exists(bootstrap))
        return std::system(("\"" + bootstrap + "\" \"" + root + "\"").c_str());
    std::cerr << "[Launcher] Bootstrap.exe not found\n";
    return 1;
}
