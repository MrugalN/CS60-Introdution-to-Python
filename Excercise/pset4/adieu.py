import inflect


def main():

    inflect = inflect.engine()
    names = []

    # Continious input from the user for name until user exit (ctrl D)
    try:
        while True:
            name = input("Name: ").strip()
            if name:
                names.append(name)
    except EOFError:
        pass

    # Formating the name list into a grammatically correct string
    farewell_message = p.join(names)

    # Print the farewell message
    print(f"Adieu, Adieu, to {farewell_message}")


if __name__ == "__main__":
    main()
