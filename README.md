# 📝 Lore Scribe

A Proof of Concept (PoC) Python desktop application that transcribes recorded TTRPG sessions and transforms them based on certain settings/preferences.

---

## 🛠️ Getting Started

### 📦 Requirements

Make sure you have the following tools installed:

- [Python](https://www.python.org/downloads/) (version `>=3.9, <3.14`)
- [`pyenv`](https://github.com/pyenv/pyenv) – Python version manager
- [`pipx`](https://github.com/pypa/pipx) – for installing CLI tools in isolated environments
- [`poetry`](https://python-poetry.org/) – dependency and virtual environment manager
- [`ffmpeg`](https://ffmpeg.org/download.html) – required by the application for audio file processing (must be installed and available on your system PATH)

---

### ⚡️ Quick Setup (Windows Users)

If you're using Windows and want to install Python, pipx, and Poetry automatically, you can use the provided PowerShell script:

```powershell
.\setup-python-env.ps1
```

> ⚠️ Run this from **PowerShell as Administrator**.  
> It will:
> - Install Python (via `pyenv-win`)
> - Install `pipx`
> - Install `poetry` via `pipx`

After running the script, you can continue from step 4 below to install dependencies and run the app.

---

### 🔁 Step-by-Step Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/lore-scribe.git
cd lore-scribe
```

#### 2. Install the Correct Python Version

Use `pyenv` to install and set the correct local Python version:

```bash
pyenv install 3.11.8
pyenv local 3.11.8
```

> This creates a `.python-version` file so that Poetry uses this Python version.

#### 3. Install Poetry (via pipx)

If you haven't already installed Poetry:

```bash
pipx install poetry
```

To update Poetry later:

```bash
pipx upgrade poetry
```

#### 4. Install Dependencies

From the root of the project (where `pyproject.toml` is located):

```bash
poetry install
```

> This creates a virtual environment and installs all required dependencies including PySide6 and pydub. Make sure `ffmpeg` is installed separately and accessible from your system's PATH.

#### 5. Run the Application

```bash
poetry run python app.py
```

---

### 💡 Optional: Use the Poetry Shell

You can also enter a subshell with the environment activated:

```bash
poetry shell
python app.py
```

> Exit the shell at any time by typing `exit`.

---

### 📁 Project Structure

```
lore-scribe/
├── app.py
├── pyproject.toml
├── README.md
└── ...
```

---

### ✅ Troubleshooting

- **`ModuleNotFoundError: No module named 'PySide6'`**

  Ensure you are running your script inside the Poetry environment using:

  ```bash
  poetry run python app.py
  ```

  Or activate the shell first:

  ```bash
  poetry shell
  ```

- **Wrong Python version?**

  Run:

  ```bash
  pyenv versions
  ```

  Then set the version again with:

  ```bash
  pyenv local 3.11.8
  ```

- **Your IDE doesn't recognize `PySide6`?**

  You may need to point your IDE (e.g. VS Code) to the correct interpreter. Find it with:

  ```bash
  poetry env info --path
  ```

  Use that path in your IDE's interpreter settings.

- **`ffmpeg` is not recognized?**

  Ensure `ffmpeg` is [downloaded](https://ffmpeg.org/download.html) and that its `bin/` folder is added to your system PATH. You should be able to run `ffmpeg -version` from your terminal.

---

## 📬 Questions or Feedback

Feel free to open an issue or PR if you run into problems or want to contribute!
