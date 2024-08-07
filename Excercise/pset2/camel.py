def main():
    # Prompt the user for the camel case variable name
    camel_case = input("camelCase: ")

    # Convert to snake case
    snake_case = camel_to_snake(camel_case)

    # Output the snake case variable name
    print(f"snake_case: {snake_case}")


def camel_to_snake(camel_case):
    snake_case = ""
    first_char = True
    for c in camel_case:
        if c.isupper() and not first_char:
            snake_case += "_" + c.lower()
        else:
            snake_case += c.lower()
            first_char = False
    return snake_case


main()
