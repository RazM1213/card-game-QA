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