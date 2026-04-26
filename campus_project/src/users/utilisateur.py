from abc import abstractmethod


class Utilisateur:
    __id = 0
    _count = 0

    def __init__(self, nom: str):
        self.__nom = nom
        self.__id += Utilisateur._count
        Utilisateur._count += 1

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def peut_valider(self, competence_id: int) -> bool:
        pass

    def get_nom(self) -> str:
        return self.__nom

    def get_id(self) -> int:
        return self.__id
