def main():
    # For loop
    names = ["Mario", "Lugi", "Daisy", "Yoshi"]
    for name in names:
        print(write_letter(name, "Princess Peach"))


def write_letter(receiver, sender):
    return f"""
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    Dear {receiver},
    
    You are cordially invited to a ball at
    Peach's Castle this evening, 7:00 PM.
    
    Sincerely,
    {sender}

+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+


"""


main()
