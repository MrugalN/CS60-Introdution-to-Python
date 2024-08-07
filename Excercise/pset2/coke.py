def main():
    total_amount_due = 50

    while total_amount_due > 0:
        insert_coin = int(input("Insert Coin: "))

        if insert_coin in [25, 10, 5]:
            total_amount_due -= insert_coin

            if total_amount_due > 0:
                print(f"Amount Due: {total_amount_due}")
            else:
                change_owed = abs(total_amount_due)
                if change_owed > 0:
                    print(f"Change Owed: {change_owed}")
                else:
                    print("Change Owed: 0")
        else:
            print(f"Amount Due: {total_amount_due}")


main()
