import nbformat
from nbclient import NotebookClient
from colorama import Fore, Style, init

init()

def verifier_et_executer_etape(notebook, etapes_a_verifier):
    with open(notebook, encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    # Marquer les cellules à ne pas exécuter
    for cell in nb.cells:
        if cell.cell_type == 'code':
            if 'tags' not in cell.metadata:
                cell.metadata['tags'] = ['skip']
            else:
                cell.metadata['tags'].append('skip')

    # Retirer le tag 'skip' pour les cellules à exécuter
    for cell in nb.cells:
        if cell.cell_type == 'markdown' and any(etape in cell.source for etape in etapes_a_verifier):
            index = nb.cells.index(cell) + 1
            if index < len(nb.cells) and nb.cells[index].cell_type == 'code':
                if 'tags' in nb.cells[index].metadata and 'skip' in nb.cells[index].metadata['tags']:
                    nb.cells[index].metadata['tags'].remove('skip')

    # Exécuter le notebook en entier
    client = NotebookClient(nb, timeout=600, kernel_name='python3')
    try:
        client.execute()
        print(Fore.GREEN + "Succès: Toutes les étapes spécifiées ont été exécutées avec succès." + Style.RESET_ALL)
    except Exception as e:
        import traceback
        print(Fore.RED + f"Erreur lors de l'exécution des cellules de code: {e}" + Style.RESET_ALL)
        print(traceback.format_exc())
        return False

    return True

if __name__ == "__main__":
    notebook_path = 'Fusilier_Antoine_1_notebook_112023.ipynb'
    etapes_a_verifier = [
        '# 1. Exploration initiale des données ',
        '## 1.1. Importation des bibliothèques nécessaires',
        '## 1.2 Paramétrages des methodes de bibliothèques (si nécessaire)',
        '## 1.3 Chargement des données ',
        '### 1.4.1 Visualiser les premières et dernières lignes de donnnées',
        '### 1.4.2. Analyse des types de données',
        '### 1.4.3. Statistiques descriptives',
        '#### 1.4.3.1. Résumé statistique',
        '#### 1.4.3.2. Fréquence et modes',
        '#### 1.4.3.3. Mesure de tendance centrale',
        '#### 1.4.3.4. Mesure de dispersion',
        '#### 1.4.3.5. Mesure de forme de distribution',
        '#### 1.4.3.6. Corrélations et tableaux croisés',
        '# 2. Préparation et Nettoyage des Données',
        '## 2.1. Identification des colonnes avec données manquantes',
        '## 2.2 Suppression des colonnes avec plus de 50% de valeurs null',
        '## 2.3 Évaluation de la pertinence des colonnes restantes',
        '## 2.4. Sélection et découpage des colonnes pertinentes',
        '## 2.5 Nettoyage et filtrage des colonnes',
        '## 2.6. Suppression des colonnes non nécessaires pour l\'analyse',
        '# 3 Nettoyage approfondi des données.',
        '## 3.1. Gestion des valeurs manquantes et doublons',
        '### 3.1.1. Suppression des lignes nulles pour des colonnes clés',
        '### 3.1.2. Suppression des doublons basés sur des identifiants uniques',
        '## 3.2 Traitement des valeurs aberrantes',
        '### 3.2.1. Gestion des NAN et valeurs aberrantes pour certaines mesures',
        '### 3.2.2. Détection et traitement des outliers',
        '## 3.4. Validation de la cohérence des données',
        '### 3.4.1. Vérification des valeurs numériques',
        '### 3.4.2. Cohérence des données additives',
        '### 3.4.3. Vérification de la cohérence des grades de nutriscore',
        '### 3.4.4. Contrôle des estimations',
        '### 3.4.5. Vérification de la cohérence des noms de produits et marques',
        '### 3.4.6. Vérification des noms de pays',
        '### 3.4.7. Validation des codes produits',
        '# 4. Imputation des Valeurs Manquantes',
        '## 4.1. Imputation par la médiane',
        '## 4.2. Imputation par la moyenne',
        '## 4.3. Imputation par KNN',
        '# 5. Vérification Post-Imputation',
        '## 5.1. Ré-évaluation des statistiques descriptives',
        '## 5.2. Vérification de la distribution des données imputées',
        '# 6. Exportation des Données Nettoyées',
        '## 6.1. Préparation du format de sortie',
        '## 6.2. Exportation des données nettoyées pour une utilisation ultérieure',

        # Ajoutez ici les autres étapes à vérifier
    ]

    for etape in etapes_a_verifier:
        verifier_et_executer_etape(notebook_path, etape)