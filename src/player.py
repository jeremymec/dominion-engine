from uuid import uuid5, UUID

from typing import List

from card import Card

class Player:

    def __init__(self, name: str) -> None:
        self.name = name
        self.id: UUID = uuid5(name)
        self.deck: List[Card] = []
        self.hand: List[Card] = []
    
    def add_cards_to_deck(self, cards: List[Card]):
        self.deck = self.deck + cards

    def add_cards_to_hand(self, cards: List[Card]):
        self.hand = self.hand + cards

    