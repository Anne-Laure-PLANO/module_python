from users.utilisateur import Utilisateur


class Formateur(Utilisateur):
    def __init__(self, nom: str) -> None:
        super().__init__(nom)

    def __str__(self) -> str:
        return f"Le formateur {super().get_nom()} possède l'ID {super().get_id()}."

    def peut_valider(self, competence_id: int) -> bool:
        return True
