
# list of possible conda locations:
$conda_search = "$env:UserProfile\*conda3\shell\condabin\conda-hook.ps1",
                "$env:LOCALAPPDATA\Continuum\*conda3\shell\condabin\conda-hook.ps1",
                "C:\ProgramData\*conda3\shell\condabin\conda-hook.ps1"    

$conda_path = Resolve-Path ($conda_search.where({Test-Path $_}) | Select-Object -first 1)
echo $conda_path
