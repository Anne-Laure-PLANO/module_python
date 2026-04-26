from dataclasses import dataclass


@dataclass
class Validation:
    __id: int
    __apprenant_id: int
    __competence_id: int
    __statut: str
    __pre_valide_par: str
    __count = 0

    def __post_init__(self) -> None:
        self.__id = type(self).__count
        type(self).__count += 1

    @property
    def id(self) -> int:
        return self.__id

    @property
    def apprenant_id(self) -> int:
        return self.__apprenant_id

    @property
    def competence_id(self) -> int:
        return self.__competence_id

    @property
    def statut(self) -> str:
        return self.__statut

    @property
    def pre_valide_par(self) -> str:
        return self.__pre_valide_par
