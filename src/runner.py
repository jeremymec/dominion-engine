from card import Card
from effect.add_to_deck import AddToDeck
from game import Game
from player import Player

from typing import Set, List

from decks import get_cards_from_decks

def run_game(player_names: Set[str], deck_names: Set[str]):

    # Create players from arguments
    players: List[Player] = []
    for name in player_names:
        players.append(Player(name))

    # Get cards in deck
    cards: List[Card] = get_cards_from_decks(set(''))

    # Create game
    game: Game = Game(players=players, cards=cards)

    # Distrbute starting cards to players
    for player in game.players:
        game.add_effect(AddToDeck())

