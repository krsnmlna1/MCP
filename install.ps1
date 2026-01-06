# PC-Control MCP Installer
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   PC-Control MCP Quick Installer      " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check Python
Write-Host "Checking Python..." -NoNewline
$python = Get-Command python -ErrorAction SilentlyContinue
if ($python) {
    $ver = python --version
    Write-Host " OK ($ver)" -ForegroundColor Green
} else {
    Write-Host " NOT FOUND!" -ForegroundColor Red
    Write-Host "Please install Python from https://python.org"
    pause
    exit
}

# Install dependencies
Write-Host ""
Write-Host "Installing dependencies..." -ForegroundColor Cyan
pip install -r requirements.txt

# Get current path
$currentPath = Get-Location
$mainPyPath = Join-Path $currentPath "main.py"

# Configure Claude
$configPath = "$env:APPDATA\Claude\claude_desktop_config.json"
Write-Host ""
Write-Host "Claude config location:" -ForegroundColor Cyan
Write-Host $configPath
Write-Host ""
Write-Host "Add this to your config:" -ForegroundColor Yellow
Write-Host @"
{
  "mcpServers": {
    "pc-control": {
      "command": "python",
      "args": ["$($mainPyPath.Replace('\','/'))" ]
    }
  }
}
"@ -ForegroundColor White

Write-Host ""
Write-Host "Installation complete!" -ForegroundColor Green
Write-Host "Remember to restart Claude Desktop!" -ForegroundColor Yellow
pause
