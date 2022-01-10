from CardGame import CardGame

# Get the 2 players names, number of cards to deal - by input from the user:
player1 = input("Enter player 1 name: ")
player2 = input("Enter player 2 name: ")
num_of_cards = int(input("How many cards to hand to each player? "))

# Create CardGame object with the data received from the user:
game = CardGame(player1, player2, num_of_cards)

# Print game-start statements:
print(f"Each player has {num_of_cards} cards... ")
print(f"{game.player1.name}'s cards: {game.player1.cards}")
print(f"{game.player2.name}'s cards: {game.player2.cards}\n")

# MAIN GAME LOOP:
for i in range(1, 11):
    print(f"=====ROUND {i}=====")
    player1_card = game.player1.get_card()
    player2_card = game.player2.get_card()
    print(f"{game.player1} threw {player1_card} to the table !")
    print(f"{game.player2} threw {player2_card} to the table !")
    if player1_card > player2_card:
        game.player1.cards.append(player1_card)
        game.player1.cards.append(player2_card)
        print(f"{game.player1.name} WINS !\n")
    else:
        game.player2.cards.append(player1_card)
        game.player2.cards.append(player2_card)
        print(f"{game.player2.name} WINS !\n")

# GAME RESULTS:
winner = game.get_winner()
print("=====FINAL RESULTS=====\n")
if winner == game.player1:
    print(f"{game.player1.name} WON THE GAME with {len(game.player1.cards)} cards !")
    print(f"{game.player1.cards}")
elif winner == game.player2:
    print(f"{game.player2.name} WON THE GAME with {len(game.player2.cards)} cards !")
    print(f"{game.player2.cards}")
else:
    print("IT'S A TIE !")