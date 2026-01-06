# PC-Control MCP Release Builder
param(
    [string]$version = ""
)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   PC-Control MCP Release Builder      " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Get version
if ($version -eq "") {
    $version = Read-Host "Enter version (e.g., 1.1.0)"
}

Write-Host "Building version: $version" -ForegroundColor Green
Write-Host ""

# Clean build folder
Write-Host "Cleaning build folder..." -NoNewline
Remove-Item "build/" -Recurse -Force -ErrorAction SilentlyContinue
New-Item -Path "build/pc-control-mcp" -ItemType Directory -Force | Out-Null
Write-Host " Done" -ForegroundColor Green

# Copy files
Write-Host "Copying files..." -NoNewline
$filesToCopy = @(
    "main.py",
    "requirements.txt",
    "README.md",
    "install.ps1",
    "tools",
    "debug_audio.py",
    "verify_tools.py"
)

foreach ($file in $filesToCopy) {
    if (Test-Path $file) {
        Copy-Item $file "build/pc-control-mcp/$file" -Recurse -Force
    }
}
Write-Host " Done" -ForegroundColor Green

# Remove cache
Write-Host "Cleaning cache..." -NoNewline
Remove-Item "build/pc-control-mcp/tools/__pycache__" -Recurse -Force -ErrorAction SilentlyContinue
Write-Host " Done" -ForegroundColor Green

# Create ZIP
Write-Host "Creating ZIP..." -NoNewline
$zipName = "pc-control-mcp-v$version.zip"
$releasePath = "../releases/$zipName"
Compress-Archive -Path "build/pc-control-mcp/*" -DestinationPath $releasePath -Force
Write-Host " Done" -ForegroundColor Green

# Cleanup
Write-Host "Cleaning up..." -NoNewline
Remove-Item "build/" -Recurse -Force
Write-Host " Done" -ForegroundColor Green

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "   Release Created Successfully!        " -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "File: $releasePath" -ForegroundColor Cyan
Write-Host "Size: $((Get-Item $releasePath).Length / 1KB) KB" -ForegroundColor Cyan
Write-Host ""
Write-Host "Ready to share!" -ForegroundColor Yellow
