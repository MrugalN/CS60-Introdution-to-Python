menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():
    total = 0.00

    while True:
        try:
            # Taking the input from the user
            item = input("Item: ").title()

            # Checking input given by user is in menu dictonary
            if item in menu:

                # Adding the price of the item to the total
                total += menu[item]

                # Showing the total amount in $ with two decimal
                print(f"Total: ${total:.2f}")

        except EOFError:
            # After the input of Control-D breaking out of the loop
            print()  # Moveing to next line
            break


main()
