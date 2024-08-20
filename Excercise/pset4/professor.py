import random


def get_level():
    while True:
        try:
            level = int(input("level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")


def main():
    level = get_level()
    score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        tries = 0
        while tries > 3:
            try:
                user_answer = int(input(f"{x} +{y} = "))
                if answer == user_answer:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            tries += 1

        if tries == 3:
            print(f"{x} +{y} = {answer} ")

    print(f"Score: {score}")


if __name__ == "__main__":
    main()
