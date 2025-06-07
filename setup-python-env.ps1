# Set strict mode and verbose output
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# Set up environment variables
$env:PYENV_ROOT = "$env:USERPROFILE\.pyenv"
$env:PATH = "$env:PYENV_ROOT\pyenv-win\bin;$env:PYENV_ROOT\pyenv-win\shims;$env:PATH"

# Function to install pyenv-win
function Install-Pyenv {
    if (-Not (Test-Path "$env:PYENV_ROOT\pyenv-win")) {
        Write-Host "Installing pyenv-win..."
        git clone https://github.com/pyenv-win/pyenv-win.git "$env:PYENV_ROOT\pyenv-win"
    } else {
        Write-Host "pyenv-win already installed."
    }
}

# Function to install latest stable Python using pyenv
function Install-Python {
    pyenv update
    $latestPython = pyenv install --list | Select-String '^\s*3\.\d+\.\d+$' | Sort-Object -Descending | Select-Object -First 1
    $version = $latestPython.ToString().Trim()
    Write-Host "Installing Python $version..."
    pyenv install $version
    pyenv global $version
}

# Function to install pipx
function Install-Pipx {
    Write-Host "Installing pipx..."
    python -m ensurepip --upgrade
    python -m pip install --upgrade pip
    python -m pip install pipx
    python -m pipx ensurepath
    $env:PATH = "$env:USERPROFILE\.local\bin;$env:PATH"
}

# Function to install poetry via pipx
function Install-Poetry {
    Write-Host "Installing Poetry with pipx..."
    pipx install poetry
}

# Execute setup
Install-Pyenv
Invoke-Expression "pyenv rehash"
Invoke-Expression "pyenv init"
Install-Python
Install-Pipx
Install-Poetry

Write-Host "`n✅ Python environment setup complete!"
Write-Host "   Python version: $(python --version)"
Write-Host "   Poetry version: $(poetry --version)"
