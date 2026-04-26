from comp.competence import Competence
from promo.promotion import Promotion
from users.apprenant import Apprenant
from users.formateur import Formateur

from fastapi import FastAPI
from routes.root import router as root_router
app = FastAPI()
app.include_router(root_router)


if __name__ == "__main__":
    campus : Promotion = Promotion("Le Campus Numérique")

    competences = [
        Competence("Python"),
        Competence("Java"),
        Competence("C++"),
        Competence("HTML"),
        Competence("CSS"),
        Competence("JavaScript"),
        Competence("SQL"),
        Competence("Django"),
        Competence("Flask"),
        Competence("Git"),
        Competence("Linux"),
        Competence("Docker"),
        Competence("Kubernetes"),
        Competence("Data Science"),
        Competence("Machine Learning"),
        Competence("Deep Learning"),
        Competence("Networking"),
        Competence("Cybersecurity"),
        Competence("Cloud Computing"),
        Competence("Agile Methodology"),
    ]

    jerome: Formateur = Formateur("Jérôme")
    print(jerome.__str__())
    answer: bool = jerome.peut_valider(competences[0].id)
    print(f"{jerome.get_nom()} peut valider : {answer}")

    Anne: Apprenant = Apprenant("Anne", campus)
    Anne.competence = competences[0]
    print(Anne.__str__())
    Anne.display_competences()
    answer2: bool = Anne.peut_valider(competences[0].id)
    print(f"{Anne.get_nom()} peut valider : {answer2}")
