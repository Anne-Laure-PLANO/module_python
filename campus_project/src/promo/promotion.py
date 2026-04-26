from users.utilisateur import Utilisateur


class Promotion:
    __liste_utilisateurs: list[Utilisateur]

    def __init__(self, utilisateurs: list[Utilisateur] = None) -> None:
        self.__liste_utilisateurs = utilisateurs or []

    def __add__(self, autre: Promotion) -> Promotion:
        return Promotion(self.utilisateurs + autre.utilisateurs)

    def ajouter_utilisateur(self, utilisateur: Utilisateur) -> None:
        if not self.utilisateurs:
            self.utilisateurs[0] = utilisateur
            print("Utilisateur ajouté à la liste.")
        else:
            if utilisateur not in self.utilisateurs:
                self.utilisateurs.append(utilisateur)
                print("Utilisateur ajouté à la liste.")
            else:
                print("L'users est déjà présent dans la liste.")

    @property
    def utilisateurs(self) -> list[Utilisateur]:
        return self.__liste_utilisateurs

    @utilisateurs.setter
    def utilisateurs(self, nouvelle_liste: list[Utilisateur] = []) -> None:
        self.__liste_utilisateurs = nouvelle_liste


