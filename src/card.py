from enum import Enum
from typing import List
from effect import Effect
from __future__ import annotations

class CardType(Enum):
    ACTION = 1
    TREASURE = 2
    VICTORY = 3

class Card:
    
    def __init__(self, name: str, type: CardType, cost: int, effects: List[Effect], description: str):
        self.name = name
        self.type = type
        self.cost = cost
        self.effects = effects
        self.description = description

    def copy_of(self) -> Card:
        return Card(self.name, self.type, self.cost, self.effects, self.description)