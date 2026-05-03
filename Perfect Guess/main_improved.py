import random
import winsound
winsound.Beep(1000, 500)

leaderboard = []

class GuessingGame:

    def __init__(self):
        self.high_score = None

    def choose_difficulty(self):

        print("\n1. Easy   (1-50)")
        print("2. Medium (1-100)")
        print("3. Hard   (1-200)")

        choice = input("Choose difficulty: ")

        if choice == "1":
            return 50
        elif choice == "2":
            return 100
        else:
            return 200

    def play(self):

        player_name = input("\nEnter your name: ")

        max_number = self.choose_difficulty()

        secret_number = random.randint(1, max_number)

        guesses = 0
        guess = -1

        print(f"\nGuess the number between 1 and {max_number}")

        while guess != secret_number:

            guess = int(input("Enter guess: "))
            guesses += 1

            if guess > secret_number:
                print("Lower!")

                # Wrong guess sound
                winsound.Beep(400, 200)

            elif guess < secret_number:
                print("Higher!")

                # Wrong guess sound
                winsound.Beep(400, 200)

        # Winning sound
        winsound.Beep(1000, 500)

        print(f"\n🎉 Correct! You guessed in {guesses} attempts.")

        # High score tracking
        if self.high_score is None or guesses < self.high_score:
            self.high_score = guesses
            print("🏆 New High Score!")

        # Add to leaderboard
        leaderboard.append((player_name, guesses))

        # Sort leaderboard
        leaderboard.sort(key=lambda x: x[1])

        # Save leaderboard to file
        with open("leaderboard.txt", "w") as file:

            for player, score in leaderboard:
                file.write(f"{player} - {score} guesses\n")

        # Display leaderboard
        print("\n===== LEADERBOARD =====")

        for rank, (player, score) in enumerate(leaderboard, start=1):
            print(f"{rank}. {player} - {score} guesses")

        print("\nBest Score:", self.high_score)


game = GuessingGame()

while True:

    game.play()

    again = input("\nPlay again? (yes/no): ")

    if again.lower() != "yes":
        print("Thanks for playing!")
        break