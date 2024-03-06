Imputation par la Moyenne ou la Médiane :

Pour les données symétriquement distribuées : L'imputation par la moyenne peut être appropriée.
Pour les données avec des valeurs extrêmes : L'imputation par la médiane est souvent préférée car elle est moins sensible aux valeurs aberrantes.
Suppression des données :

Si le pourcentage de valeurs manquantes est faible, la suppression des lignes (ou des colonnes si le problème est très localisé) peut être envisagée. Cependant, cela peut entraîner une perte d'informations précieuses.
Imputation par le Mode :

Pour les données catégorielles ou discrètes, l'imputation par le mode (la valeur la plus fréquente) peut être une option.
K-Nearest Neighbors (KNN) Imputer :

Cette méthode peut être utile si les données sont suffisamment denses et si on observe des tendances ou des groupements naturels dans l'espace des caractéristiques. Par exemple, des produits alimentaires similaires pourraient avoir des profils nutritionnels similaires.
Imputation par chaîne multiple (MICE) :

Cette méthode est utile si l'on soupçonne que les valeurs manquantes sont liées à d'autres variables dans le jeu de données. Par exemple, le contenu en fibres pourrait être prédit en fonction d'autres variables nutritionnelles.
Considération des valeurs spécifiques au domaine :

Dans certaines situations, il peut être justifié d'imputer des valeurs spécifiques qui sont pertinentes pour le domaine d'étude. Par exemple, si une valeur manquante dans fruits-vegetables-nuts-estimate-from-ingredients_100g pourrait raisonnablement être zéro pour certains produits.
Examen des motifs de valeurs manquantes :

Parfois, les valeurs manquantes ne sont pas aléatoires. Par exemple, si les aliments plus transformés ont tendance à avoir moins d'informations sur les fruits, les légumes et les noix, cette information pourrait être utile pour l'imputation ou l'analyse.