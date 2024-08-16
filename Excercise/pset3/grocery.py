def main():
    grocery_list = {}

    while True:
        try:
            # Input from the user converted in upper case            
            item = input().strip().upper()

            # Checking for items in the list, increment its count
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                # For new item add it to dictionary
                grocery_list[item] = 1

        except EOFError:
            # Breaking Loop
            print()
            break

    # Sort the items alphabetically and print them
    for item in sorted(grocery_list.keys()):
        print(f"{grocery_list[item]} {item}")
    
main()
