import random

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
VALUES = {rank: index + 2 for index, rank in enumerate(RANKS)}

deck = [{'rank' : rank, 'suit': suit, 'value': VALUES[rank]} for suit in SUITS for rank in RANKS]
random.shuffle(deck)

mid = len(deck) // 2
player_deck = deck[:mid]
computer_deck = deck[mid:]

def play_round():
    global player_deck, computer_deck
    if not player_deck:
        print("You lose!")
        return False
    if not computer_deck:
        print("You win!")
        return False

    player_card = player_deck.pop(0)
    computer_card = computer_deck.pop(0)

    print(f"You played: {player_card['rank']} of {player_card['suit']}")
    print(f"Computer player: {computer_card['rank']} of {computer_card['suit']}")

    table_pile = [player_card, computer_card]

    if player_card['value'] > computer_card['value']:
        player_deck.extend(table_pile)
        print("You win the round.")
    elif player_card['value'] < computer_card['value']:
        computer_deck.extend(table_pile)
        print("You lose the round.")
    else:
        print("War!")
        handle_war()

    input("Press enter to play")

    return True

def handle_war():
    global player_deck, computer_deck
    if len(player_deck) < 4:
        print("Not enough cards for war, you lose!")
        return
    if len(computer_deck) < 4:
        print("Computer does not have enough cards for war, you win!")
        return 
    
    player_war_cards = [player_deck.pop(0) for _ in range(4)]
    computer_war_cards = [computer_deck.pop(0) for _ in range(4)]

    table_pile.extend(player_war_cards + computer_war_cards)

    print(f"You played face-up card: {player_war_cards[-1]['rank']} of {player_war_cards[-1]['suit']}")
    print(f"Computer played face-up card: {computer_war_cards[-1]['rank']} of {computer_war_cards[-1]['suit']}")

    if player_war_cards[-1]['value'] > computer_war_cards[-1]['value']:
        player_deck.extend(table_pile)
        print("You win the war!")
    elif player_war_cards[-1]['value'] < computer_war_cards[-1]['value']:
        computer_deck.extend(table_pile)
        print("You lose the war!")
    else:
        print("Another war!")
        handle_war(table_pile)
    
def play_game():
    while True:
        if not play_round():
            break
    print ("Game over!")

if __name__ == "__main__":
    play_game()

