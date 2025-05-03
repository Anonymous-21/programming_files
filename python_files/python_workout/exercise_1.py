from random import randint


def guessing_game() -> None:
    random_num: int = randint(1, 100)
    count: int = 0
    num_of_guesses: int = 3

    while True:
        while True:
            print("Guess a number between 1 and 100: ")
            guess: int = input("> ")
            try:
                guess = int(guess)
                break
            except ValueError:
                print("Not a number")

        if guess == random_num:
            print("Just right")
            break
        elif guess < random_num:
            print("Too low")
        elif guess > random_num:
            print("Too high")

        count += 1

        if count >= num_of_guesses:
            print(f"You have guessed {num_of_guesses} times already.")
            break


guessing_game()
