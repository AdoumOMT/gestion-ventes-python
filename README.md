# Gestion des ventes avec Python

Mini-projet réalisé durant ma première année de formation afin de mettre en pratique les bases de la programmation Python, la création d'une interface graphique et la manipulation d'une base de données SQLite.

## Présentation

Cette application est une petite interface desktop permettant de gérer des données de ventes.

Elle permet notamment de :

* créer une base de données SQLite ;
* afficher les données enregistrées ;
* ajouter une nouvelle vente ;
* rechercher une vente à partir de son identifiant ;
* modifier une vente existante ;
* supprimer une vente.

Ce projet correspond à mes premières expériences avec Python et les bases de données. Il constitue une étape dans mon évolution vers des projets informatiques plus complets.

## Technologies utilisées

* **Python**
* **Tkinter** — création de l'interface graphique
* **SQLite** — gestion de la base de données
* **sqlite3** — connexion entre Python et SQLite

## Fonctionnalités

### 1. Création de la base de données

L'application permet de créer automatiquement une base de données SQLite nommée `ventes.db`.

La table principale utilisée est :

`ventes_clean`

Elle contient les informations suivantes :

| Champ    | Type    | Description        |
| -------- | ------- | ------------------ |
| ID       | INTEGER | Identifiant unique |
| Date     | DATE    | Date de la vente   |
| Product  | TEXT    | Nom du produit     |
| Price    | REAL    | Prix du produit    |
| Quantity | INTEGER | Quantité vendue    |
| Region   | TEXT    | Région             |

### 2. Ajouter une vente

L'utilisateur peut saisir :

* la date ;
* le produit ;
* le prix ;
* la quantité ;
* la région.

Les informations sont ensuite enregistrées dans la base SQLite.

### 3. Afficher les ventes

L'application permet d'afficher les différentes ventes enregistrées dans la base de données.

### 4. Rechercher une vente

Une recherche peut être effectuée à partir de l'identifiant (`ID`) d'une vente.

### 5. Modifier une vente

L'utilisateur peut sélectionner une vente à partir de son identifiant puis modifier ses informations.

### 6. Supprimer une vente

Une vente peut être supprimée après confirmation de l'utilisateur.

## Structure du projet

```text
gestion-ventes-python/
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

### Prérequis

Il faut avoir Python installé sur son ordinateur.

Vérifier l'installation avec :

```bash
python --version
```

### Télécharger le projet

Cloner le dépôt :

```bash
git clone https://github.com/AdoumOMT/gestion-ventes-python.git
```

Puis accéder au dossier :

```bash
cd gestion-ventes-python
```

### Lancer l'application

Exécuter :

```bash
python main.py
```

La fenêtre de l'application devrait s'ouvrir.

## Utilisation

Lors du premier lancement :

1. Cliquer sur **Créer une base de Données**.
2. Cliquer sur **Ajouter** pour enregistrer une vente.
3. Utiliser **Afficher** pour consulter les données.
4. Utiliser **Rechercher** pour retrouver une vente.
5. Utiliser **Mettre à Jour** pour modifier une vente.
6. Utiliser **Supprimer** pour supprimer une vente.

La base `ventes.db` est créée localement et n'est pas incluse dans le dépôt GitHub.

## Aperçu

Une capture d'écran de l'application sera ajoutée prochainement.

## Ce que ce projet m'a permis d'apprendre

Ce projet m'a permis de découvrir et de pratiquer plusieurs notions fondamentales :

* syntaxe Python ;
* fonctions ;
* conditions ;
* gestion des exceptions ;
* interfaces graphiques avec Tkinter ;
* événements et boutons ;
* manipulation des entrées utilisateur ;
* connexion à une base de données ;
* requêtes SQL ;
* opérations CRUD ;
* organisation basique d'une application.

Les opérations CRUD correspondent à :

* **Create** — ajouter des données ;
* **Read** — consulter/rechercher des données ;
* **Update** — modifier des données ;
* **Delete** — supprimer des données.

## Limites du projet

Ce projet a été réalisé au début de ma formation. Le code reste volontairement simple et présente certaines limites, notamment :

* interface graphique basique ;
* validation limitée des données saisies ;
* architecture encore peu modulaire ;
* gestion de la base de données directement dans les fonctions de l'interface ;
* absence de système d'authentification ;
* absence de tests automatisés.

Ces limites représentent également une partie de mon évolution : les projets réalisés par la suite ont progressivement intégré une meilleure organisation du code et des fonctionnalités plus avancées.

## Évolution

Ce projet constitue l'une de mes premières réalisations en programmation.

L'objectif de la publication sur GitHub est également de conserver une trace de mon évolution au cours de ma formation, depuis mes premiers projets Python jusqu'à des applications plus complexes utilisant notamment le développement web, les bases de données et le machine learning.

---

## Auteur

**Adoum Oumar Moussa Tahir**

Étudiant en informatique — systèmes intelligents et recherche opérationnelle.

GitHub : `https://github.com/AdoumOMT`
