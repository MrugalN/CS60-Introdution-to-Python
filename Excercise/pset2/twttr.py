def main():
    # Prompt the user for input
    word_to_shorten = input("input: ")

    # Define vowels (as strings, not variables)
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    # Create a new string with vowels removed
    shortened_word = ""
    for char in word_to_shorten:
        if char not in vowels:
            shortened_word += char

    # Output the modified string
    print(f"output: {shortened_word}")


main()
