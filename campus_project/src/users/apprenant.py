from comp.competence import Competence
from promo.promotion import Promotion
from users.utilisateur import Utilisateur


class Apprenant(Utilisateur):
    def __init__(self, nom: str, promo : Promotion) -> None:
        super().__init__(nom)
        self.__promo : Promotion = promo
        self.__competence_a_valider: list[Competence] = []

    def peut_valider(self, competence_id: int) -> bool:
        if any(c.id == competence_id for c in self.__competence_a_valider):
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"L'apprenant {super().get_nom()} possède l'ID {super().get_id()}."

    @property
    def competence(self) -> list[Competence]:
        return self.__competence_a_valider

    @competence.setter
    def competence(self, nouvelle_competence: Competence) -> None:
        if (
            not self.__competence_a_valider
            or nouvelle_competence not in self.__competence_a_valider
        ):
            print(
                f"L'apprenant {self.get_nom()} est prêt(e) pour valider la compétence {nouvelle_competence.nom}. "
            )
            self.__competence_a_valider.append(nouvelle_competence)
        else:
            print(
                f"La compétence {nouvelle_competence} a déjà été validée par {self.get_nom()}."
            )

    def display_competences(self) -> None:
        print("Compétences à valider : ")
        for comp in self.__competence_a_valider:
            print(f"- {comp.nom}")

    def supprimer_competence(self, competence_a_supprimer: Competence) -> None:
        if competence_a_supprimer in self.__competence_a_valider:
            self.__competence_a_valider.remove(competence_a_supprimer)
            print(
                f"La compétence {competence_a_supprimer} a été supprimée des compétences validées de {self.get_nom()}."
            )
        else:
            print("Cette compétence n'est pas encore validée.")
