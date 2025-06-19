import art
import random

def deal_card(x):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.sample(cards, x)

def calc_score(x):
    total = sum(x)
    if len(x) == 2 and total == 21:
        return 0
    while total > 21 and 11 in x:
        for i in range(len(x)):
            if x[i] == 11:
                x[i] = 1
                break
        total = sum(x)
    return total

def compare(player, computer):
    if player == computer:
        print("It's a draw")
    elif computer == 0 and player == 0:
        print("Both have Blackjack, Computer Wins!")
    elif computer == 0:
        print("Computer wins with a Blackjack")
    elif player == 0:
        print("Win with a Blackjack")
    elif player > 21:
        print("Bust! You lose.")
    elif computer > 21:
        print("Dealer went over, you win!.")
    elif player > computer:
        print("You win")
    else:
        print("Computer wins")
    return

def play_game():
    print(art.logo)
    player_cards = deal_card(2)
    dealer_cards = deal_card(2)
    player_score = 0
    dealer_score = 0

    over = False

    while not over:
        player_score = calc_score(player_cards)
        dealer_score = calc_score(dealer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {dealer_cards[0]}")

        if dealer_score == 0 or player_score == 0 or player_score >= 21:
            over = True
        else:
            if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                temp = deal_card(1)
                player_cards.append(temp[0])
            else:
                over = True

    while dealer_score != 0 and dealer_score < 21:
        temp = deal_card(1)
        dealer_cards.append(temp[0])
        dealer_score = calc_score(dealer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
    compare(player_score, dealer_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n" *20)
    play_game()

# def play_game(): unoptimized and inefficient
#     print(logo)
#     player_cards = deal_card(2)
#     dealer_cards = deal_card(2)
#     player_score = calc_score(player_cards)
#     dealer_score = calc_score(dealer_cards)
#
#     print(f"Your cards: {player_cards}, current score: {player_score}")
#     print(f"Computer's first card: {dealer_cards[0]}")
#
#     if dealer_score == 0 and player_score == 0:
#         print("Both have Blackjack, Computer wins!")
#         return
#     elif dealer_score == 0:
#         print(f"Computer wins with a Blackjack")
#         return
#     elif player_score == 0:
#         print(f"Win with a Blackjack")
#         return
#     elif player_score > 21:
#         print(f"Bust! You lose.")
#         return
#     while player_score < 21:
#         hit = input("Type 'y' to get another card, type 'n' to pass: ")
#         if hit == 'y':
#             temp = deal_card(1)
#             player_cards.append(temp[0])
#             player_score = calc_score(player_cards)
#             print(f"Your cards: {player_cards}, current score: {player_score}")
#             print(f"Computer's first card: {dealer_cards[0]}")
#         else:
#             break
#     if player_score > 21:
#         print(f"Bust! You lose.")
#         return
#     else:
#         while dealer_score < 17:
#             temp = deal_card(1)
#             dealer_cards.append(temp[0])
#             dealer_score = calc_score(dealer_cards)
#
#     print(f"Your final hand: {player_cards}, final score: {player_score}")
#     print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
#     compare(player_score, dealer_score)
