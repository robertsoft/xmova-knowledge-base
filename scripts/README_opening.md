Como usar o `open-xmova.ps1`

Objetivo
- Abrir um projeto dentro de `C:/dev/projects/xMova Apps` junto com a `xmova-knowledge-base` e arquivos de referência, para que o Copilot e o VS Code tenham contexto completo sem modificar o projeto.

Exemplos
- Abrir pelo nome do projeto (resolvido em `C:/dev/projects/xMova Apps`):

```powershell
cd C:/xmova-knowledge-base/scripts
./open-xmova.ps1 -ProjectPath "MyApp"
```

- Abrir fornecendo caminho completo:

```powershell
./open-xmova.ps1 -ProjectPath "C:/dev/projects/xMova Apps/MyApp"
```

Notas
- Requer que o comando `code` (VS Code CLI) esteja disponível no PATH. No VS Code: Command Palette → "Shell Command: Install 'code' command in PATH".
- O script abre as pastas em uma única janela (multi-root) e também abre alguns arquivos-chave da knowledge-base.
- Se preferir usar um workspace fixo, abra `C:/xmova-knowledge-base/xmova.code-workspace`.
 - Requer que o comando `code` (VS Code CLI) esteja disponível no PATH. No VS Code: Command Palette → "Shell Command: Install 'code' command in PATH".
 - O script abre as pastas em uma única janela (multi-root) e também abre alguns arquivos-chave da knowledge-base.
 - Se preferir usar um workspace fixo, abra `C:/xmova-knowledge-base/xmova.code-workspace`.

Opções de build automático
- Para acionar automaticamente um build ao abrir o projeto, use o parâmetro `-RunBuild` (tenta disparar a tarefa de build do VS Code via `code --command workbench.action.tasks.build`).
- Para executar um comando de build diretamente (sem depender do VS Code), use `-BuildCommand` seguido do comando a executar (ex.: `"python build.py"` ou `"./xmova_compiler.exe build"`).

Exemplos
```powershell
./open-xmova.ps1 -ProjectPath "MyApp" -RunBuild
./open-xmova.ps1 -ProjectPath "MyApp" -BuildCommand "./xmova_compiler.exe --compile"
```

Observações
- A opção `-RunBuild` depende do suporte do `code` CLI para `--command`; se não funcionar, use `-BuildCommand` com o comando do compilador.
- O build executado com `-BuildCommand` roda no PowerShell fora do VS Code — útil para compilar rapidamente sem modificar projetos.
