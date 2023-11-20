$python = Get-Command python -ErrorAction SilentlyContinue
if ($python) {
    $version = python --version
    Write-Host "Python installé : $version"
} else {
    Write-Host "Python n'est pas installé."
}

# Informe l'utilisateur sur la façon d'obtenir la dernière version de Python
Write-Host "Pour télécharger la dernière version de Python, rendez-vous sur : https://www.python.org/downloads/"
Write-Host "Assurez-vous de télécharger la version correspondant à votre système (Windows 32 bits ou 64 bits)."