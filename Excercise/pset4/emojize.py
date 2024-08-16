from ast import alias
import emoji


def main():

    user_input = input("Input = ")

    emojized = emoji.emojize(user_input, language="alias")

    print("output:", emojized)


main()
