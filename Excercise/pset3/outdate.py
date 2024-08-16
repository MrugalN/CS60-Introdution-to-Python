months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    while True:
        date = input("Date: ").strip()

        try:  # checking the format of the input date "MM/DD/YYY"
            if "/" in date:
                month, day, year = date.split("/")
                month, day, year = int(month), int(day), int(year)

            else:  # checking for the format of input date "Month DD, YYYY"
                if "," not in date:
                    raise ValueError  # If there's no comma, raise an error

                # Split the date based on the comma and process the month and year separately
                month_day, year = date.split(",", 1)

                # Strip any leading/trailing spaces from the year
                year = year.strip()

                # Now split month_day to get month and day separately
                month_part, day = month_day.split()

                # Convert the month name to a number
                month = months.index(month_part) + 1

                # Convert day to an integer
                day = int(day)
                year = int(year)

            # Checking for the valid date
            if month < 1 or month > 12 or day < 1 or day > 31:
                raise ValueError

            # Printing the date in the format YYYY-MM-DD with leading zeros
            print(f"{year}-{month:02}-{day:02}")
            break

        except (ValueError, IndexError):
            # Catch any invalid date format and invalid month names (reprompt)
            continue


main()
