# CloudIDE / Coding Platform

A modern, web-based Integrated Development Environment (IDE) featuring code editing, workspace management, and advanced backend language features. 

The project is architected as a decoupled system featuring a reactive web **Frontend** and a robust Python-based **Backend** powered by Language Server Protocol (LSP) integration.

---

## ✨ Features

* **Advanced Code Workspace**: Features an extensible `Editor` and a split `EditorPane` layout.
* **Workspace Management**: Integrated `Sidebar` navigation, operational `StatusBar`, and a dedicated `ProblemsPanel` for error diagnostics and coding tasks.
* **Intelligent Backend**: Robust file management, search capabilities, and Language Server Protocol (`lsp`) integration for smart code intelligence.
* **Integrated API Terminal**: Executes code and manages terminal inputs/outputs directly from the browser.

---

## 🛠️ Architecture & Tech Stack

The repository is organized into a monorepo-style structure separating the presentation and application layers:

* **Frontend**: Powered by Node.js/React ecosystem. Uses modern design utilities, custom CSS modules, and `lucide-react` icons for a clean, developer-focused user experience.
* **Backend**: Powered by Python (`main.py`). Handles core computation, terminal environments, search algorithms, and LSP orchestration.

---

## 🤝 Contributing

We welcome contributions to improve the IDE! Please review our [CONTRIBUTING.md](./CONTRIBUTING.md) before making any modifications. 

### Development Workflow:
1. Ensure your `.gitignore` is correctly configured so that heavy build artifacts like `node_modules` or `__pycache__` are never tracked.
2. Follow the **Conventional Commits** specification for all commit messages (e.g., `feat(frontend): ...`, `fix(backend): ...`).

---

## 📄 License

This project is licensed under the terms specified in the [LICENSE](./LICENSE) file.
