def main():
    # Prompt the user for a greeting
    greeting = input("Greetings: ").strip()

    # Get the value based on the greeting
    result = value(greeting)

    # Print the result
    print(f"${result}")


def value(greeting):
    # Convert the greeting to lowercase to handle case insensitivity
    greeting = greeting.lower()

    # Check if the greeting starts with "hello"
    if greeting.startswith("hello"):
        return 0
    # Check if the greeting starts with "h" but is not "hello"
    elif greeting.startswith("h"):
        return 20
    # For all other cases
    else:
        return 100


if __name__ == "__main__":
    main()
