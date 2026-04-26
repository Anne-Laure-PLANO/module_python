from dataclasses import dataclass


@dataclass
class Competence:
    __nom: str
    __id: int = 0
    _count = 0

    def __post_init__(self) -> None:
        self.__id += type(self)._count
        type(self)._count += 1

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, nom: str) -> None:
        self.__nom = nom
