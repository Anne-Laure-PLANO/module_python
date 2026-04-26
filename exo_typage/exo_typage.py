from typing import TypedDict


class Apprenant(TypedDict):
    nom: str
    promo: str
    competences: list[str]


def creer_apprenant(nom: str, promo: str) -> Apprenant:
    return {"nom": nom, "promo": promo, "competences": []}


def valider_competence(apprenant: Apprenant, competence: str) -> None:
    if competence not in apprenant["competences"]:
        apprenant["competences"].append(competence)


def peut_valider(apprenant: Apprenant, competence: str) -> bool:
    return competence in apprenant["competences"]


def afficher_progression(apprenants: list[Apprenant]) -> None:
    for a in apprenants:
        nb: int = len(a["competences"])
        print(f"{a['nom']} : {nb} compétence(s) validée(s)")


def trouver_par_nom(apprenants: list[Apprenant], nom: str) -> Apprenant | None:
    for a in apprenants:
        if a["nom"] == nom:
            return a
    return None


def statistiques(apprenants: list[Apprenant]) -> float | None:
    total = 0
    for a in apprenants:
        total += len(a["competences"])
    if len(apprenants) == 0:
        return 0
    return total / len(apprenants)
