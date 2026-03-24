import random

# CARD CONFIG

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

# GAME CONFIG

player_turn = True
dealers_turn = False

# OTHER CONFIGS

DEBUG = False

# VARIABLES

rounds = 0

# HANDS

dealers_hand = []
players_hand = []

# DECK CONFIGURATION

# CREATE DECK
def create_deck():
    deck = [(rank, suit) for suit in suits for rank in ranks]
    DEBUG and print("Deck Created with 52 Cards.")
    return deck

# SHUFFLE DECK
def shuffle_deck(deck):
    random.shuffle(deck)
    DEBUG and print("Deck Shuffled.")
    return deck
    
deck = create_deck()
deck = shuffle_deck(deck)

# GAME PLAY

# DEAL CARDS
def deal_card(deck):
    card = deck.pop()
    DEBUG and print(f"Dealt card: {card[0]} of {card[1]}")
    if player_turn:
        players_hand.append(card)
        DEBUG and print(f"Player's Hand: {players_hand}")
        DEBUG and print(f"Player's Hand Value: {calculate_hand_score(players_hand)}")
    else:
        dealers_hand.append(card)
        DEBUG and print(f"Dealer's Hand: {dealers_hand}")
        DEBUG and print(f"Dealer's Hand Value: {calculate_hand_score(dealers_hand)}")

# CALC SCORE (CALC IS SLANG FOR CALCULATE or whatever)
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

# JUST HERE TO BE HERE
def play_game():
    handle_round()
    return None

# WHERE THE GAME ACC GOES
def handle_round():
    _players_turn = False
    _dealers_turn = False

    if player_turn:
        _players_turn = True
        deal_card(deck)
        deal_card(deck)
        while _players_turn:
            if 21 > calculate_hand_score(players_hand):
                print(f"Current Hand: {', '.join(f'{rank} of {suit}' for rank, suit in players_hand)} - Total: " + str(calculate_hand_score(players_hand))) # idk what this print statement is tbh it just works ig
                option = input("Would you like to hit or stand? ")
                option.lower()
                if option == "hit":
                    deal_card(deck)
            else:
                _players_turn = False
                handle_win("Player")

def handle_win(player):
    print(player + " has won the round.")

if __name__ == "__main__":
    play_game()
