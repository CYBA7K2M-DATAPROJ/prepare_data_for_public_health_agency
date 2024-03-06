Suppression des données :

Suppression des lignes : Éliminer les lignes qui contiennent des valeurs manquantes.
Suppression des colonnes : Retirer les colonnes qui présentent un nombre élevé de valeurs manquantes.
Imputation de valeurs :

Imputation par la moyenne : Remplacer les valeurs manquantes par la moyenne de la colonne.
Imputation par la médiane : Utilisée surtout pour les données avec des valeurs extrêmes, où la médiane est plus représentative.
Imputation par le mode : Convient pour les données catégorielles, remplaçant par la valeur la plus fréquente.
Imputation par une valeur constante : Remplacer les valeurs manquantes par une valeur constante qui a du sens pour le contexte des données.
Imputation basée sur des modèles :

Imputation par régression : Utiliser les autres variables pour prédire les valeurs manquantes à l'aide d'un modèle de régression.
K-Nearest Neighbors (KNN) Imputer : Remplacer par la moyenne ou la médiane des k voisins les plus proches.
Imputation par chaîne multiple (Multiple Imputation by Chained Equations, MICE) : Une méthode plus sophistiquée qui modélise chaque variable avec des valeurs manquantes comme une fonction des autres variables, et utilise cela pour l'imputation.
Utilisation d'algorithmes tolérants aux valeurs manquantes :

Certains algorithmes de machine learning, comme les arbres de décision et leurs dérivés (Random Forests, Gradient Boosting Machines), peuvent gérer les valeurs manquantes sans imputation préalable.
Imputation basée sur le temps :

Pour les séries temporelles, l'imputation peut se faire en utilisant la dernière valeur disponible (carry forward) ou la prochaine valeur connue (carry backward).
Imputation stochastique :

Remplacer les valeurs manquantes par un échantillon aléatoire tiré de la distribution des données observées.