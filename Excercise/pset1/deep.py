def main():
    answer = (
        input(
            "What is the answer to the Great Question of Life, the Universe and everything\n"
        )
        .strip()
        .lower()
    )
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        print("Yes")
    else:
        print("No")


main()
