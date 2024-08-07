distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44,
}


def main():
    for name in distances.keys():  # calls out all the keys from the disctionary
        print(f"{name} is {distances[name]} AU from the earth")


main()
