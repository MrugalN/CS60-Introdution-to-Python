def main():
    difficulty = input("Difficult or Casual? \n")
    players = input("Multiplayer or Single-player? \n")

    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("poker")
        elif players == "single-player":
            recommend("Klondike")
        else:
            ("Enter a valid number of players")

    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("Hearts")
        elif players == "single-player":
            recommend("Clock")
        else:
            ("Enter a valid number of players")
    else:
        print("Enter a valid difficulty")


def recommend(game):
    print("you might like", game)


main()
