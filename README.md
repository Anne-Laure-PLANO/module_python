# module_python
Ensemble des exercices réalisés dans le cadre de ma formation au Campus Numérique In The Alps 


## Ce que j’ai réalisé pendant ce module :

--> **Jeu ShiFuMi** : Un premier projet pour me remettre dans le bain de Python après 3 semaines de Java.

--> **Devine_nombre** : Un jeu pour deviner un nombre entre 1 et 100 généré par ordinateur, avec un comptage des tentatives.

--> **Traduction des nombres en nombres romains** : Projet basé sur la méthode TDD (Test Driven Development), où l’on écrit d’abord les tests, puis on développe progressivement la solution pour passer ces tests.

--> **ToDo List avec une API REST** : Utilisation de FastAPI et Pydantic pour développer une API qui gère les données de la ToDo List, accessibles depuis le navigateur grâce à HTTPX, et rendues modifiables sans base de données grâce à Uvicorn qui héberge l'API.

## Outils transverses utilisés :

--> **pytest** pour l’automatisation des tests, en particulier pour le projet de traduction des nombres en romains.

--> **mypy** : Cet outil m’a bien servi pour vérifier le typage des variables et des fonctions. Par exemple, lorsqu’une fonction retournait un type incorrect ou que certaines variables pouvaient être None, mypy m’a permis de mieux adapter mon code.

--> **ruff** : Un outil pour vérifier et corriger l’indentation. Très utile au quotidien, mais j’ai eu une petite mésaventure : en configurant mon IDE pour exécuter ruff à chaque sauvegarde automatique, mes retours à la ligne disparaissaient dès que j’ajoutais du code entre deux fonctions !