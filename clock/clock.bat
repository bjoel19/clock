cd %~dp0

%windir%\System32\WindowsPowerShell\v1.0\powershell.exe ^
  -ExecutionPolicy ByPass ^
  -NoExit ^
  -Command ". ./find_conda.ps1; & $conda_path; cd ../../../; conda activate base; python clockgui.py"
