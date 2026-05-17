
# SetUp Local Virtual Environment (Python 3.12.3)

This project uses an isolated Python virtual environment to manage dependencies and packages.

---

## 🛠️ Prerequisites: Install Python 3.12.3

Before setting up the environment, you must have Python 3.12.3 installed on your system.

### Windows
1. Download the official installer from [Python.org (Python 3.12.3)](https://python.org).
2. Run the installer (`python-3.12.3-amd64.exe`).
3. ⚠️ **Crucial Step:** Check the box that says **"Add python.exe to PATH"** at the bottom of the installer window before clicking install.
4. Complete the installation.

### macOS
* **Using Homebrew (Recommended):** Open your terminal and run:
  ```bash
  brew install python@3.12
  ```
* **Official Installer:** Download and run the macOS 64-bit installer from [Python.org (Python 3.12.3)](https://python.org).

### Linux (Ubuntu/Debian)
Open your terminal and run the following commands to add the deadsnakes PPA and install Python 3.12:
```bash
sudo alt-get update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12 python3.12-venv
```

### Verify Installation
Open a new terminal window and verify that the correct version is installed:
```bash
python3.12 --version
```
*(On Windows, if you used the installer, `python --version` should also work).*

---

## 🚀 Environment Setup

### 1. Create the Environment
To create the virtual environment using Python 3.12.3 with the folder name `env`, run:
```bash
python3.12 -m venv env
```

### 2. Activate the Environment
Activate the environment based on your operating system and shell:

* **Windows (PowerShell):**
  ```powershell
  env\Scripts\Activate.ps1
  ```
* **Windows (Git Bash / Command Prompt):**
  ```bash
  source env/Scripts/activate
  ```
* **macOS / Linux:**
  ```bash
  source env/bin/activate
  ```
*(Once activated, you will see `(env)` at the beginning of your terminal prompt).*

### 3. Deactivate the Environment
To leave the virtual environment and return to global Python, simply run:
```bash
deactivate
```

---

## 💻 VS Code Configuration

To make sure VS Code uses the correct Python interpreter and recognizes installed packages:

1. Press `Ctrl + Shift + P` (Mac: `Cmd + Shift + P`) to open the Command Palette.
2. Search for and select **Python: Select Interpreter**.
3. Choose the option pointing to your local environment: `./env/bin/python` or `.\env\Scripts\python.exe`.

---

## 📦 Package Management

* **Install project dependencies:** `pip install -r requirements.txt`
* **Save new dependencies:** `pip freeze > requirements.txt`

> ⚠️ **Important:** Never push the `env/` folder to GitHub. Ensure that `env/` is added to your `.gitignore` file.
