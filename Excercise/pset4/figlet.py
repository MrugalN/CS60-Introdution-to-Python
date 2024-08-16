import sys
import random
from pyfiglet import Figlet


def main():
    figlet = Figlet()

    # Get the available fonts
    available_fonts = figlet.getFonts()

    # Check the number of command-line arguments
    if len(sys.argv) == 1:
        # No arguments provided, choose a random font
        font = random.choice(available_fonts)
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        # Two arguments provided, check if the font is valid
        if sys.argv[2] in available_fonts:
            font = sys.argv[2]
        else:
            sys.exit("Error: Font not found.")
    else:
        sys.exit("Usage: python figlet.py [-f | --font] [font_name]")

    # Set the font
    figlet.setFont(font=font)

    # Prompt the user for input
    text = input("Input: ")

    # Render and print the text in the chosen font
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()
