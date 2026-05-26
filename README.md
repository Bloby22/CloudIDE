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

## 🚀 Getting Started

### Prerequisites
* **Node.js** (v18.0 or higher recommended)
* **Python** (v3.10 or higher recommended)
* **Git**

### 1. Frontend Setup
Navigate to the frontend directory to install and start the web interface:
```bash
# Install dependencies
npm install

# Start the local development server
npm run dev
```

### 2. Backend Setup
Navigate to the root or backend directory to configure the Python application:
```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install required packages (if a requirements.txt is present)
pip install -r requirements.txt

# Run the backend server
python main.py
```

---

## 🤝 Contributing

We welcome contributions to improve the IDE! Please review our [CONTRIBUTING.md](./CONTRIBUTING.md) before making any modifications. 

### Development Workflow:
1. Ensure your `.gitignore` is correctly configured so that heavy build artifacts like `node_modules` or `__pycache__` are never tracked.
2. Follow the **Conventional Commits** specification for all commit messages (e.g., `feat(frontend): ...`, `fix(backend): ...`).

---

## 📄 License

This project is licensed under the terms specified in the [LICENSE](./LICENSE) file.
