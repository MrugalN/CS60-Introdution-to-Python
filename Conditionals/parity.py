from numpy import true_divide


def main():
    x = int(input("What's x? \n"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0

    # return True if n % 2 == 0 else False

    # if n % 2 == 0:
    #     return True
    # else:
    #     return False


main()
