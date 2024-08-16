def main():
    while True:
        try:
            fraction = input("Fraction: ")
            # Spliting the input into x and y
            x, y = fraction.split("/")

            # Coverting x and y into integers
            x = int(x)
            y = int(y)

            # Checking if y is 0
            if y == 0:
                raise ZeroDivisionError

            # Checking if x is greater than y
            if x > y:
                raise ValueError

            # Calculating the percentage
            percentage = (x / y) * 100

            # Checking the output based on the percentage
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{round(percentage)}%")
            break

        except ValueError:
            print("Numerator is greater than denominator. Please try again.")
        except ZeroDivisionError:
            print("Fraction cannot have zero in denominator. Please try again.")


main()
