from typing import List

from player import Player
from card import Card
from effect.effect import Effect

class Game:

    def __init__(self, players: List[Player], cards: List[Card]) -> None:
        self.players = players
        self.cards = cards
        self.effect_stack = []
    
    def add_effect(self, effect: Effect):
        self.effect_stack.append(effect)
    
    def process_effect(self):
        effect: Effect = self.effect_stack.pop()
        effect.execute(self)