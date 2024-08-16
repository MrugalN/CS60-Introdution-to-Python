def main():
    x = get_int("What's the x? ")
    print(f"x is {x}")


def get_int(promt):
    while True:
        try:
            return int(input(promt))  # promt help in making the code more useable

        except ValueError:  # catch the value error try and except:
            pass  # just pass the nuber but does not provide any information


main()

# print(f"x is {x}")
