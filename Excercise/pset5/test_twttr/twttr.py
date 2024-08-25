def main():
    # Prompt the user for input
    word_to_shorten = input("Input: ")

    # Use the shorten function to remove vowels
    shortened_word = shorten(word_to_shorten)

    # Output the modified string
    print(f"Output: {shortened_word}")


def shorten(word):
    # Define vowels (as strings, not variables)
    vowels = "aeiouAEIOU"

    # Create a new string with vowels removed
    shortened_word = ""
    for char in word:
        if char not in vowels:
            shortened_word += char

    return shortened_word


if __name__ == "__main__":
    main()
