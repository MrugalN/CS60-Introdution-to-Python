from multiprocessing import Value
import random


def get_positive_integer(promt):
    """Prompt the user for a positive integer"""
    while True:
        try:
            value = int(input(promt))
            if value > 0:
                return value
        except ValueError:
            pass  # Ignore the error and prompt again


def main():
    # Promt to input user for level
    level = get_positive_integer("Level: ")

    # Generate random number between 1 and level
    secret_number = random.randint(1, level)

    # Checking with the  guess number:

    while True:
        guess = get_positive_integer("Guess: ")

        # Hint to secrete number

        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too large!")
        else:
            print("Just right!")
            break


if __name__ == "__main__":
    main()
