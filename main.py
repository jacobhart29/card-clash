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

rounds = 1

# HANDS

dealers_hand = []
players_hand = []

# DECK CONFIGURATION

# CREATE DECK
def create_deck():
    deck = [(rank, suit) for suit in suits for rank in ranks]
    DEBUG and print("Deck Created with 52 Cards.")
    return deck

# SHUFFLE DECK (Takes the deck to shuffle it)
def shuffle_deck(deck):
    random.shuffle(deck)
    DEBUG and print("Deck Shuffled.")
    return deck
    
deck = create_deck()
deck = shuffle_deck(deck)

# GAME PLAY

# DEAL CARDS (Takes the main deck and add the cards to the hand that is listed)
def deal_card(deck, hand):
    card = deck.pop()
    DEBUG and print(f"Dealt card: {card[0]} of {card[1]}")
    if hand == "player":
        players_hand.append(card)
        DEBUG and print(f"Player's Hand: {players_hand}")
        DEBUG and print(f"Player's Hand Value: {calculate_hand_score(players_hand)}")
    elif hand == "dealer":
        dealers_hand.append(card)
        DEBUG and print(f"Dealer's Hand: {dealers_hand}")
        DEBUG and print(f"Dealer's Hand Value: {calculate_hand_score(dealers_hand)}")
    else: DEBUG and print("Failed to give card to:" + hand)

# CALC SCORE (CALC IS SLANG FOR CALCULATE or whatever) and it takes a hand variables which is the player/dealers deck
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

# JUST HERE TO BE HERE (Handles round starts and ends and resets the game if the player wants to play again)
def play_game():
    global deck, player_turn, dealers_turn, players_hand, dealers_hand
    while True:
        handle_round()
        compare_scores()
        print("*" * 61)
        print("Round: " + str(rounds))
        players_hand.clear()
        dealers_hand.clear()
        player_turn = True
        dealers_turn = False
        if len(deck) < 20:
            DEBUG and print("Deck is low on cards. Reshuffling...")
            deck = create_deck()
            deck = shuffle_deck(deck)
    return None

# WHERE THE GAME ACC GOES (It uses the gloabal variables to keep track)
def handle_round():
    global player_turn, dealers_turn, rounds, deck
    rounds += 1
    _players_turn = False
    _dealers_turn = False
    deck = shuffle_deck(deck)
    deal_card(deck, "player")
    deal_card(deck, "player")
    deal_card(deck, "dealer")
    deal_card(deck, "dealer")

    if player_turn:
        _players_turn = True
        while _players_turn:
            if 21 >= calculate_hand_score(players_hand):
                print(f"Current Hand: {', '.join(f'{rank} of {suit}' for rank, suit in players_hand)} - Total: " + str(calculate_hand_score(players_hand)))
                d_rank, d_suit = dealers_hand[0]
                print(f"The Dealers First Card is {d_rank} of {d_suit}.")
                option = input("Would you like to hit or stand? ")
                newOPTION = option.lower()
                if newOPTION == "hit":
                    deal_card(deck, "player")
                elif newOPTION == "stand":
                    _players_turn = False
                    player_turn = False
                    _dealers_turn = True
                    dealers_turn = True
                    
                else:
                    print("Like ACC pick Hit or Stand")
            else:
                _players_turn = False
                player_turn = False
                _dealers_turn = True
                dealers_turn = True
                print("You Busted - Total: " + str(calculate_hand_score(players_hand)))
    
    if dealers_turn:
        while _dealers_turn:
            if 17 >= calculate_hand_score(dealers_hand):
                deal_card(deck, "dealer")
                DEBUG and print("DEALER HIT")
            else: 
                DEBUG and print("DEALER STAND AT " + str(calculate_hand_score(dealers_hand)))
                _players_turn = False
                player_turn = False
                _dealers_turn = False
                dealers_turn = False

# JUST TO BE CLEAN IG
def handle_win(player):
    print(player + " has won the round.")

# WIN CONDITIONS (Just checks for has more or who didn't bust)
def compare_scores():
    p_score = calculate_hand_score(players_hand)
    d_score = calculate_hand_score(dealers_hand)
    print(f"Final Scores - Player: {p_score} | Dealer: {d_score}")

    # i rewrote the entire win logic just cuz i could and to fix it
    if p_score > 21 and d_score > 21:
        print("Both bust! It's a Push (tie).")

    elif p_score > 21:
        handle_win("Dealer")

    elif d_score > 21:
        handle_win("Player")

    else:
        if p_score > d_score:
            handle_win("Player")
        elif d_score > p_score:
            handle_win("Dealer")
        else:
            print("Push (tie).")

if __name__ == "__main__":
    print("Round: " + str(rounds))
    play_game()

#END
