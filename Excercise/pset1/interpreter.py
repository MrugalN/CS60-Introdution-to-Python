def main():
    # Taking input from the user
    expression = input("Expression: ").strip()

    # Splitting the input from user in variabels
    x, y, z = expression.split(" ")

    # Converting x and z into integers
    x = int(x)
    z = int(z)

    # Arthmatic opertions

    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z
    else:
        print("Invalid operator")
        return

    # print the output of the arithmatic operation
    print(f"{result:.1f}")


main()
