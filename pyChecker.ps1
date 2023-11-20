$python = Get-Command python -ErrorAction SilentlyContinue
if ($python) {
    $version = python --version
    Write-Host "Python installé : $version"
} else {
    Write-Host "Python n'est pas installé."
}
Write-Host "Pour télécharger la dernière version de Python, rendez-vous sur : https://www.python.org/downloads/"