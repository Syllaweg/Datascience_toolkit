# Datascience_toolkit
boite à outils pour les library tel que Pandas, Numpy, etc...

Ce n’est pas un projet de développement classique et il a donc ses propres contraintes mais surtout il aura besoin d’une grande souplesse et de réajustements réguliers.

## Définition des objectifs
- Accès & Analyse des données
- Préparation des données
- Modélisation
- Evaluation et scoring (Itération)
- Déploiement (Ré-évaluation régulière/Itération)

## Etape N°1 : Définition des objectifs
Si cette étape peut paraître évidente elle n’en n’est pas moins vitale pour la réussite du projet. Au delà de la problématique métier sous-jacente il s’agit ici de déterminer de quel typologie de problème nous devons résoudre.

Pour cela nous devons savoir si nous avons des données d’expérimentation avec résultat ou non (voire partiels) afin de déterminer si nous abordons un problème de type supervisé ou non-supervisé.

Ensuite quelle est la typologie du problème à résoudre :

- Régression
- Classification
- Clustering
- Classement (ranking)
- Système de recommandations
- Réduction du nombre de dimension
Pour avoir plus de détails sur ces problèmes de Machine Learning. Si vous êtes perdu n’hésitez pas à vous référer au memento des algorithmes de Machine Learning de datacorner.fr

## Etape N°2 : Accès & Analyse des données
Étape cruciale dans laquelle il faut retravailler les données (features ou variables). C’est une opération indispensable car les algorithmes de Machine Learning n’acceptent pas tout type de données. 
C’est une opération nécessaire afin d’affiner les variables pour qu’elles soient mieux gérées par ces mêmes algorithmes.

### Découpage du jeu de données
Tout d’abord vous travaillez avec un jeu de données. Vous allez devoir le découper en deux parties (minimum) :

- Données d’entraînement : sous-ensemble destiné à l’apprentissage d’un modèle.
- Données de test : sous-ensemble destiné à l’évaluation du modèle. Ce jeu de données ne doit en aucun cas être utilisé lors de la conception du modèle !
Ce découpage vous allez le gérer à partir de fonctions prédéfinies (sklearn.model_selection.train_test_split). Mais rien n’est jamais si simple car la manière dont vous allez découper votre jeu de données peut avoir une importance trop grande sur votre modèle.
Il faudra faire tester plusieurs possibilités (ex. sklearn.model_selection.KFold).

### Analyse des données

- Faire un inventaire de vos données (type de données) :
- Typologie : Numériques, temporelles, textes, binaires, etc.
- Variables catégorielles, discrètes ou continues ?
- Nombre d’observations (nombre de lignes) ?
- Nombre de features/variables (nombre de colonnes) ?
- Détecter si vous avez des outliers et surtout décider de ce que vous allez en faire (les supprimer ou simplement les altérer)
- Détecter les valeurs manquantes
- Détection de variables/features corrélées
A ce niveau là il est indispensable de disposer d’un bon outil de dataviz !

## Etape N°3 : Préparation des données
L’étape N°2 permettant de faire un état des lieux complet des données dont vous disposez, vous allez devoir maintenant préparer vos features/variables afin qu’elles soient utilisables par des algorithmes de Machine Learning.

Pour reprendre les points précédent :

Vous ne devez avoir des données (variables) qu’au format numériques. si vous avez des données de type :
Date : Appliquez des formules pour les transformer en période, etc. Pourquoi ne pas ajouter des agrégations sur des fenêtres glissantes (sur la semaine, le mois, l’année qui a précédé) ?
Catégorielles: utilisez l’encodage One-Hot dans la mesure du possible. Si vous avez trop de variables, réduisez le scope en faisant des regroupement.
Texte: il vous faudra certainement découper, reformater vos données pour avoir des données catégorielles
Si vous avez des informations manquantes (Null)
Supprimez la ligne entière si vous avez vraiment beaucoup de données (déconseillé mais parfois vous n’aurez pas le choix)
Remplacez les par une valeurs, la valeur médiane, la moyenne, etc.
Mettez à l’echelle les valeurs numériques (feature scaling)
Passer au logarithme lorsque les variables ont des valeurs extrêmes, cela réduit leur importance.
On appelle aussi cette étape le feature engineering !

Un autre aspect important est la gestion de ses jeux de données : la création des jeux de données de travail. Si vous avez un jeu de données unique vous allez devoir constituer un jeu de données d’entraînement et un jeu de test !

## Etape N°4 : La modélisation
Lors de cette étape vous allez choisir le ou plutôt les algorithmes de Machine Learning qui vous semblent les mieux adaptés.

Selon le problème que vous allez traiter, vous avez le choix des algorithmes, piochez et testez donc ! Cette phase peut être longue (temps) car l’entraînement est une tâche très lourde surtout dés lors que l’on a beaucoup de données (ce qui est par ailleurs conseillé).

La difficulté n’est pas dans ce choix mais plutôt dans l’ajustement des hyperparamètres que vous allez devoir faire afin d’obtenir un modèle performant.

## Etape N°5 : Evaluation & scoring
Votre algorithme choisit ainsir que les hyper-paramètres ajustés, vous allez devoir valider votre modèle. Impossible de ne pas entrer dans un mode itératif dans lequel vous allez tatoner avec ces hyper-parametres.
N’hésitez pas ici à faire appel à des outils tiers ou des approches comme la recherche par gille (grid-search).

Attention surtout à l’over-fitting (ou sur-entraînement) qui vous donnera l’illusion d’un bon modèle !

En effet si vous dépasser un certain score (au alentours de 95%) il est probable que votre modèle soit ultra-performant … mais que pour vos données d’entraînement. Essayez le donc avec les données de test … vous serez certainement surpris !

En ce qui concerne la manière de mesurer les performances elle diffère selon le type de problème mais aussi selon ce que vous voulez vraiment mesurer. Plusieurs mesures sont disponibles (liste non exhaustive):

Classification
Matrice de confusion
Courbe ROC
Précision / Rappel
Régression
Erreur de prédiction
Graphe XY valeur à prédire / valeur prédite
Clustering
Variance intra classe, inter classe
Nombre d’arc coupés
Vous entrez donc dans une phase d’optimisation basée sur une approche forcément itérative. Voici quelques pistes d’amélioration et/ou d’optimisation :

Changement d’algorithme
La distribution des jeux de tests/entraintement est-elle cohérente, homogène ?
Ajout/suppression de variables
Groupement de valeurs : ajouter des moyennes, somme, nombre par groupes.
Ajout/suppression de lignes (avec de nouvelles sources de données)
Ajustement des hyper-paramètres
Ajouter des combinaisons de variables difficiles à apprendre pour un modèle comme un ratio
Aggréger sur des périodes supérieure (par exemple 1 mois pour une granularité journalière) peut être une bonne piste
Utiliser la sortie d’autre modèle de machine learning.
Chercher l’information qui pourrait aider un modèle à corriger des erreurs
Etape N°6 : Déploiement
Votre modèle est prêt. il est performant et peut se plier à tous les cas de figure. Vous pouvez maintenant le déployer au travers d’une API ou l’intégrer directement dans un programme. Attention cependant, car par nature un modèle ne peu vivre eternellement (il est en effet basé sur un apprentissage sur des données … et les données évoluent sans cesse). Il faut donc prévoir de vérifier régulièrement.

Voilà pour cet article qui avait pour vocation de parcourir un projet de Machine Learning type. Si vous avez besoin d’aller plus loin dans la méthodologie je vous invite à aller voir du coté de la méthode CRISP.
