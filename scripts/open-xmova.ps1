param(
  [string]$ProjectPath,
  [switch]$RunBuild,
  [string]$BuildCommand
)

# Usage:
# .\open-xmova.ps1 -ProjectPath "C:/dev/projects/xMova Apps/MyApp"
# or
# .\open-xmova.ps1 -ProjectPath "MyApp"    # will be resolved under C:/dev/projects/xMova Apps

$kb = "C:/xmova-knowledge-base"
$base = "C:/dev/projects/xMova Apps"

if (-not $ProjectPath) {
  Write-Host "Informe o caminho do projeto (nome ou caminho completo). Ex: MyApp ou C:/dev/projects/xMova Apps/MyApp"
  exit 1
}

if (-not (Test-Path $ProjectPath)) {
  # try resolving as subfolder name
  $maybe = Join-Path $base $ProjectPath
  if (Test-Path $maybe) { $ProjectPath = $maybe } else { Write-Host "Projeto não encontrado: $ProjectPath"; exit 1 }
}

# Files to open from the knowledge base (change as needed)
$kbFiles = @(
  "$kb/docs/schema/manifest-schema.json",
  "$kb/examples/starter-templates/manifest-example.yaml",
  "$kb/scripts/map_blocks_to_manifest.py"
)

# Build code CLI args: open project folder + kb folder + open files
$args = @($ProjectPath, $kb) + $kbFiles

# Try to run code CLI
$codeCmd = "code"
try {
  & $codeCmd @args
} catch {
  Write-Host "Comando 'code' não encontrado. Verifique se 'Visual Studio Code' está instalado e 'code' está no PATH."
  Write-Host "Como alternativa, abra o workspace: C:/xmova-knowledge-base/xmova.code-workspace"
}

# Optionally run a build step after opening VS Code.
# Two modes supported:
#  - provide -BuildCommand to run a shell command in the project folder (recommended for non-invasive builds)
#  - provide -RunBuild to attempt to trigger the VS Code default build task via the `code` CLI
if ($RunBuild -or $BuildCommand) {
  Start-Sleep -Seconds 2

  if ($BuildCommand) {
    Write-Host "Executando build command no projeto: $BuildCommand"
    Push-Location $ProjectPath
    try {
      Invoke-Expression $BuildCommand
    } catch {
      Write-Host "Falha ao executar BuildCommand: $_"
    }
    Pop-Location
  } elseif ($RunBuild) {
    # Try to trigger the VS Code build task (may require 'code' supporting --command)
    try {
      & $codeCmd --command "workbench.action.tasks.build"
      Write-Host "Acionada a tarefa de build no VS Code (workbench.action.tasks.build)."
    } catch {
      Write-Host "Não foi possível acionar a tarefa de build via 'code --command'. Você pode executar Ctrl+Shift+B manualmente ou fornecer -BuildCommand.'"
    }
  }
}
