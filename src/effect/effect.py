from abc import ABC, abstractmethod

from game import Game


class Effect(ABC):

    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def execute(game: Game):
        pass