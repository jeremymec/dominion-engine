from enum import Enum
from typing import Set, List

from card import Card, CardType

class Deck:

    def __init__(self, deck_names: Set[str]) -> None:
        # TODO - Complete dummy method (possibly using proper data source)
        cards: List[Card] = [Card(
            name="Copper", type=CardType.TREASURE, cost=0, effects=[], description="Copper")]

        return cards
    
    def get_card(self, name: str):
        return cards