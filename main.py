import random

# CARD CONFIG

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

# GAME CONFIG

player_turn = True
dealers_turn = False

# HANDS

dealers_hand = []
players_hand = []

# DECK CONFIGURATION

# CREATE DECK
def create_deck():
    deck = [(rank, suit) for suit in suits for rank in ranks]
    print("Deck Created with 52 Cards.")
    return deck

# SHUFFLE DECK
def shuffle_deck(deck):
    random.shuffle(deck)
    print("Deck Shuffled.")
    return deck
    
deck = create_deck()
deck = shuffle_deck(deck)

# GAME PLAY

# DEAL CARDS
def deal_card(deck):
    card = deck.pop()
    print(f"Dealt card: {card[0]} of {card[1]}")
    if player_turn:
        players_hand.append(card)
        print(f"Player's Hand: {players_hand}")
        print(f"Player's Hand Value: {calculate_hand_score(players_hand)}")
    else:
        dealers_hand.append(card)
        print(f"Dealer's Hand: {dealers_hand}")
        print(f"Dealer's Hand Value: {calculate_hand_score(dealers_hand)}")

def calculate_hand_score(hand):
    value = 0
    aces = 0
    for card in hand:
        rank = card[0]
        value += values[rank]
        if rank == "Ace":
            aces += 1
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value
