from effect.effect import Effect
from typing import List

from game import Game
from card import Card
from player import Player

class AddToHand(Effect):

    def __init__(self, card: Card, amount: int, player: Player) -> None:
        self.card = card
        self.amount = amount
        self.player = player

    def execute(self, game: Game):
        cards: List[Card] = []
        for n in range(self.amount):
            cards.append(self.card.copy_of())

        self.player.add_cards_to_hand(cards)