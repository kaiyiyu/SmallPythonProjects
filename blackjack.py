import random, sys 

# Constants
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = "backside"

def main():
    print("""Blackjack 
    
        Rules: 
            Try to get as close to 21 without going over.
            Kings, Queens, and Jacks are worth 10 points.
            Aces are worth 1 or 11 points.
            Cards 2 through 10 are worth their face value.
            (H)it to take another card.
            (S)tand to stop taking cards.
            On your first play, you can (D)ouble down to increase your bet
            but must hit exactly one more time before standing.
            In case of a tie, the bet is returned to the player.
            The dealer stops hitting at 17.""")
    
    money = 5000
    # Main game loop
    while True:
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing!')
            sys.exit()

        # Get player bet amount for the round
        print(f"Money: {money}")
        bet = get_bet()
        
        # Give player and dealer two cards each from the deck
        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]
        
        # Handle player actions
        print(f"Bet: {bet}")
        while True:
            display_hands(player_hand, dealer_hand, False)
            
        # TBC
    
# Function to get player bet for each round    
def get_bet(max_bet):
    while True:
        bet = input(f"How much do you want to bet? (1-{max_bet}) or QUIT\n> ").upper().strip()
        if bet == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        
        if not bet.isdecimal():
            print("Please enter a valid amount.")
            continue
        
        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet
        
# Function to get a list of cards in a deck
def get_deck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  # Numbered cards
        for rank in ("J", "K", "Q", "A"):
            deck.append((rank, suit))   # Face and ace cards
    random.shuffle(deck)
    return deck      
            
if __name__ == "__main__":
    main()