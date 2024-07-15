import random
import sys

# Define a list of tuples with video game options and their clues
video_games = [
    ("Super Mario Bros.", "A classic platformer featuring Mario and Luigi."),
    ("The Legend of Zelda", "An action-adventure game where you play as Link."),
    ("Pokemon Red/Blue", "A role-playing game where you catch and train Pokemon."),
    ("Minecraft", "A sandbox game where you can build and explore endless worlds."),
    ("Grand Theft Auto V", "An open-world game with a story about criminals."),
    ("The Witcher 3: Wild Hunt", "An RPG where you play as Geralt of Rivia, a monster hunter."),
    ("Overwatch", "A team-based shooter with unique characters and abilities."),
    ("Fortnite", "A battle royale game where you build and fight to be the last one standing."),
    ("Portal", "A puzzle game involving a device that creates inter-spatial portals."),
    ("Final Fantasy VII", "A classic RPG with a memorable story and characters.")
]

def play_game():
    # Pick a random video game from the list
    game_name, game_clue = random.choice(video_games)

    # Generate random incorrect options
    options = random.sample([game[0] for game in video_games if game[0] != game_name], 2)
    options.append(game_name)
    random.shuffle(options)

    print("\nWelcome to the Video Game Guessing Game!")
    print("I'm thinking of a video game... Can you guess which one it is?")
    print(f"Here's a clue: {game_clue}")
    print("\nChoose from the following options:")
    for idx, option in enumerate(options):
        print(f"{chr(65 + idx)}. {option}")

    correct_option = chr(65 + options.index(game_name))
    guesses_left = 3
    score = 0

    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")
        guess = input("Enter your choice (A, B, C): ").strip().upper()

        if guess not in {"A", "B", "C"}:
            print("Invalid input. Please enter 'A', 'B', or 'C'.")
            continue

        if guess == correct_option:
            score += 1
            print("\nCongratulations! You guessed it right! The game was", game_name)
            break
        else:
            print("Wrong guess! Try again.")
            guesses_left -= 1

    if guesses_left == 0:
        print("\nSorry, you ran out of guesses. The correct game was", game_name)

    return score

def main():
    total_score = 0
    total_games = 0

    while True:
        total_games += 1
        score = play_game()
        total_score += score

        print(f"\nGame Stats: Total Games: {total_games}, Total Score: {total_score}, Average Score: {total_score / total_games:.2f}")

        while True:
            play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if play_again in {"yes", "no"}:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if play_again == "no":
            break

    print("\nThanks for playing the Video Game Guessing Game!")
    sys.exit()

if __name__ == "__main__":
    main()
