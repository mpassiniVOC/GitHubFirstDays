import random

def roll_dice():
    """Simulate rolling two dice."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2


def play_game():
    print("🎲 Welcome to the Dice Roll Game! 🎲")

    # Roll the dice
    die1, die2 = roll_dice()

    # Player chooses
    choice = input("Do you pick the first die or the second? (1 or 2): ").strip()

    if choice == "1":
        player_roll = die1
        computer_roll = die2
    elif choice == "2":
        player_roll = die2
        computer_roll = die1
    else:
        print("Invalid choice! You must enter 1 or 2.")
        return

    # Show results
    print(f"\nYou rolled: {player_roll}")
    print(f"Computer rolled: {computer_roll}")

    # Determine winner
    if player_roll > computer_roll:
        print("🎉 You win!")
    elif player_roll < computer_roll:
        print("💻 Computer wins!")
    else:
        print("🤝 It's a tie!")


# Run the game
play_game()
