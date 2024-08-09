def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # 1. Length must be between 2 and 6 characters.
    if not 2 <= len(plate) <= 6:
        return False

    # 2. Must start with atleast 2 character.
    if not plate[0:2].isalpha():
        return False

    # 3. No periods, spaces, or punctuation marks are allowed.
    if not plate.isalnum():
        return False

    # 4. Numbers to be at end of the plate and cannot start with 0.
    num_start = False
    for i, char in enumerate(plate):
        if char.isdigit():
            if char == "0" and not num_start:
                return False  # first number cannot be 0
            num_start = True
        elif num_start:
            return False  # No letter after numbers

    return True


main()
