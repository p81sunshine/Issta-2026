from solution import *
import math

def test_all():
    random.seed(42)
    card = Card("Hearts", "Ace")
    assert str(card) == "Ace of Hearts"

    deck = Deck()
    assert len(deck.cards) == 52

    first_card = deck.cards[0]
    assert str(first_card) == "2 of Spades"

    deck.shuffle()
    shuffled_first_card = deck.cards[0]
    assert str(shuffled_first_card) != "2 of Spades"

    drawn_card = deck.draw()
    assert str(drawn_card) == str(shuffled_first_card)
    assert len(deck.cards) == 51

    alice = Player("Alice")
    assert alice.name == "Alice"
    assert len(alice.hand) == 0

    card = Card("Clubs", "10")
    alice.receive_card(card)
    assert len(alice.hand) == 1
    assert "10 of Clubs" in alice.show_hand()

    # add 2 more cards
    alice.receive_card(Card("Clubs", "Jack"))
    alice.receive_card(Card("Clubs", "Queen"))
    assert len(alice.hand) == 3
    assert "Jack of Clubs" == alice.hand[1].__str__()
    assert "Queen of Clubs" == alice.hand[2].__str__()

    game = Game(['Alice', 'Bob'])
    for player in game.players:
        assert len(player.hand) == 0

    game.distribute_cards()
    total_cards = sum([len(player.hand) for player in game.players])
    assert total_cards == 52
    assert len(game.players[0].hand) == 26
    assert len(game.players[1].hand) == 26

    # draw all cards from the deck
    while game.deck.cards:
        game.deck.draw()

    assert len(game.deck.cards) == 0
    # try to draw, should return None
    assert game.deck.draw() is None

    # show all hands
    hands = game.show_all_hands()
    assert len(hands) == 2
    assert len(hands[0]) == 26
    assert len(hands[1]) == 26