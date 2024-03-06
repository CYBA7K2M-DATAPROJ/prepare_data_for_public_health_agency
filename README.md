# Project 3 - Prepare data for public health agency

File to download for resource folder :
https://s3-eu-west-1.amazonaws.com/static.oc-static.com/prod/courses/files/parcours-data-scientist/P2/fr.openfoodfacts.org.products.csv.zip

# Introduction

## Présentation du contexte métier

Avec l'essor des préoccupations alimentaires, tant en termes de santé que d'environnement, les consommateurs sont de plus en plus soucieux de connaître la provenance, la composition et l'impact de leurs achats alimentaires. Open Food Facts est une base de données collaborative sur les produits alimentaires du monde entier. Elle fournit des informations détaillées sur la composition nutritionnelle, les ingrédients, les allergènes, etc. Ces données sont essentielles pour de nombreuses parties prenantes :

Consommateurs : cherchant à prendre des décisions d'achat éclairées.
Entreprises : souhaitant améliorer leurs produits ou cibler des marchés spécifiques.
Chercheurs : analysant les tendances alimentaires et leurs impacts sur la santé publique.


## Objectif de l'analyse
1. Nettoyage des données : Étant une base de données collaborative, Open Food Facts peut contenir des erreurs, des doublons ou des informations manquantes. Notre premier objectif est de nettoyer et de préparer ces données pour une analyse approfondie.

2. Caractérisation des produits : Analyser la composition nutritionnelle des produits, identifier les produits les plus sains et ceux qui pourraient présenter des risques pour la santé.

3. Identification des tendances : Déceler des patterns ou des tendances parmi les produits, comme la prévalence d'ingrédients spécifiques ou les tendances nutritionnelles par pays ou par type de produit.

4. Compliance RGPD : Même si nous travaillons avec des données sur des produits et non sur des individus, il est essentiel de veiller à ce que notre traitement des données soit conforme aux normes et régulations en vigueur.

## Étapes de préparation et nettoyage des données

1. Exploration Initiale des Données
   - 1.1. Importation des bibliothèques nécessaires
   - 1.2. Paramétrages des méthodes de bibliothèques (si nécessaire)
   - 1.3. Chargement des données
   - 1.4. Visualisation initiale des données
     - 1.4.1. Affichage des premières et dernières lignes
     - 1.4.2. Analyse des types de données
     - 1.4.3. Statistiques descriptives
       - 1.4.3.1. Résumé statistique
       - 1.4.3.2. Fréquence et modes
       - 1.4.3.3. Mesure de tendance centrale
       - 1.4.3.4. Mesure de dispersion
       - 1.4.3.5. Mesure de forme de distribution
       - 1.4.3.6. Corrélations et tableaux croisés
       - 1.4.3.7. Graphiques et visualisations
   - 1.5. Identification Préliminaire des Anomalies

2. Préparation et Nettoyage des Données
   - 2.1. Identification des colonnes avec données manquantes
   - 2.2. Suppression des colonnes avec plus de 50% de valeurs nulles
   - 2.3. Évaluation de la pertinence des colonnes restantes
   - 2.4. Sélection et découpage des colonnes pertinentes
   - 2.5. Nettoyage et filtrage des colonnes
   - 2.6. Suppression des colonnes non nécessaires pour l'analyse
   - 2.7. Exploration des Relations entre les Colonnes
   - 2.8. Analyse de sensibilité initiale

3. Nettoyage Approfondi des Données
   - 3.1. Gestion des valeurs manquantes et doublons
     - 3.1.1. Suppression des lignes nulles pour des colonnes clés
     - 3.1.2. Suppression des doublons basés sur des identifiants uniques
   - 3.2. Normalisation et transformation des données
       - 3.2.1. Normalisation des données numériques
       - 3.2.2. Normalisation des données textuelles
   - 3.3. Traitement des valeurs aberrantes
     - 3.3.1. Gestion des NAN et valeurs aberrantes pour certaines mesures
     - 3.3.2. Détection et traitement des outliers
   - 3.4. Validation de la cohérence des données
     - 3.4.1. Vérification des valeurs numériques
     - 3.4.2. Cohérence des données additives
     - 3.4.3. Vérification de la cohérence des grades de nutriscore
     - 3.4.4. Contrôle des estimations
     - 3.4.5. Vérification de la cohérence des noms de produits et marques
     - 3.4.6. Vérification des noms de pays
     - 3.4.7. Validation des codes produits
   - 3.5. Exploration de la dimensionnalité

4. Imputation des Valeurs Manquantes
   - 4.1. Imputation par la médiane
   - 4.2. Imputation par la moyenne
   - 4.3. Imputation par KNN
   - 4.4. Évaluation comparative des méthodes d'imputation

5. Vérification Post-Imputation
   - 5.1. Ré-évaluation des statistiques descriptives
   - 5.2. Vérification de la distribution des données imputées
   - 5.3. Tests de robustesse post-imputation
   - 5.4. Validation Croisée
   
6. Exportation des Données Nettoyées
   - 6.1. Préparation du format de sortie
   - 6.2. Exportation des données nettoyées pour une utilisation ultérieure
   - 6.3. Documentation détaillée des modifications (README)

## Analyse des données et visualisation global

Pour structurer ces trois parties dans un notebook de manière organisée et détaillée, voici comment vous pourriez diviser chacune d'elles en sous-parties :

### 1. Définition des Objectifs de l'Analyse

#### 1.1 Précision des Objectifs
- **1.1.1 Introduction et Contexte** : Brève introduction expliquant le contexte et l'importance de l'analyse.
- **1.1.2 Formulation des Objectifs** : Énumération précise des questions de recherche ou objectifs commerciaux.
- **1.1.3 Attentes et Livrables** : Définir ce qui est attendu comme résultat de l'analyse.

#### 1.2 Identification des Variables et Hypothèses
- **1.2.1 Inventaire des Données Disponibles** : Liste des datasets disponibles et description sommaire.
- **1.2.2 Sélection des Variables Clés** : Identifier les variables principales pour l'analyse.
- **1.2.3 Formulation des Hypothèses** : Établir des hypothèses basées sur la compréhension initiale des données.

### 2. Analyse Exploratoire des Données (AED)

#### 2.1 Analyse Quantitative
- **2.1.1 Statistiques Descriptives** : Calcul et interprétation des mesures de tendance centrale et de dispersion.
- **2.1.2 Analyse de Distributions** : Visualisation des distributions de données (histogrammes, boîtes à moustaches).
- **2.1.3 Exploration de Tendances et Patterns** : Identifier des tendances ou des modèles dans les séries temporelles ou autres types de données.

#### 2.2 Analyse Qualitative
- **2.2.1 Identification de Motifs et Catégories** : Rechercher des motifs récurrents ou des catégories distinctes dans les données.
- **2.2.2 Analyse des Anomalies** : Détecter et explorer les anomalies ou les valeurs aberrantes.

#### 2.3 Outils d'AED
- **2.3.1 Utilisation de Pandas Profiling** : Génération de rapports automatisés avec `pandas_profiling`.
- **2.3.2 Visualisations Interactives** : Utiliser des outils comme Plotly pour des visualisations interactives.

### 3. Analyse Statistique Approfondie

#### 3.1 Tests Statistiques
- **3.1.1 Choix des Tests Statistiques** : Sélectionner les tests appropriés en fonction des hypothèses et du type de données.
- **3.1.2 Mise en Œuvre des Tests** : Réaliser des tests t, chi-carré, etc., et interpréter les résultats.

#### 3.2 Modèles de Régression
- **3.2.1 Construction de Modèles de Régression** : Développer des modèles linéaires ou logistiques.
- **3.2.2 Évaluation des Modèles** : Analyser la performance des modèles (R², p-valeurs, etc.).

#### 3.3 Analyse Multivariée
- **3.3.1 Techniques de Réduction de Dimension** : Appliquer l'ACP ou d'autres méthodes pour résumer les données.
- **3.3.2 Interprétation des Résultats Multivariés** : Expliquer les résultats des analyses factorielles ou ACP en termes compréhensibles.

Chacune de ces sous-parties doit être accompagnée de code, de visualisations et de commentaires explicatifs pour assurer la clarté et la pertinence de l'analyse. Cela fournira un guide étape par étape pour mener une analyse de données complète et approfondie.
#### 4. Visualisation des Données
- **Visualisations Avancées** : Créer des cartes géographiques, des graphiques en radar, des treemaps pour des visualisations plus complexes.
- **Interactivité** : Utiliser des outils comme Bokeh ou Dash pour créer des visualisations interactives.

#### 5. Modélisation Prédictive
- **Choix de Modèles** : Sélectionner des modèles appropriés en fonction du problème (classification, régression, clustering).
- **Feature Engineering** : Créer et sélectionner des caractéristiques pertinentes pour améliorer la performance du modèle.
- **Optimisation de Modèle** : Utiliser la recherche en grille ou la recherche aléatoire pour l'hyperparamétrage.

#### 6. Validation des Modèles
- **Techniques de Validation** : Utiliser des méthodes comme K-fold cross-validation pour évaluer la généralisabilité.
- **Analyse de Performance** : Interpréter des métriques de performance contextualisées selon le problème spécifique.

#### 7. Interprétation des Résultats
- **Insights Basés sur les Données** : Traduire les résultats statistiques en insights compréhensibles et actionnables.
- **Impact sur les Décisions** : Évaluer comment les résultats peuvent influencer les stratégies ou les décisions commerciales.

#### 8. Rapport et Présentation des Résultats
- **Présentations Engageantes** : Utiliser des outils comme PowerPoint ou Google Slides avec des visualisations intégrées pour des présentations claires.
- **Rapports Écrits** : Rédiger des rapports détaillés avec des sections clairement définies, des résumés et des annexes.

#### 9. Prise de Décision Basée sur les Données
- **Stratégies Basées sur les Données** : Développer des recommandations stratégiques basées sur l'analyse pour guider les décisions opérationnelles ou commerciales.
- **Planification d'Actions** : Proposer un plan d'actions concrètes basé sur les résultats analytiques.

#### 10. Partage et Collaboration
- **Partage des Connaissances** : Organiser des ateliers ou des séminaires pour partager les résultats avec des équipes ou des parties prenantes.
- **Outils Collaboratifs** : Utiliser des plateformes comme GitHub, Google Drive pour le partage de documents et la collaboration en équipe.
