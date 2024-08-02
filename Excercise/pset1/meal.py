def main():
    # Checking input time from the user
    time = input("what time is it? ").strip()

    # converting the time input in float
    hours = convert(time)

    # Determining the meal time from the input time from the user
    if 7 <= hours <= 8:
        print("Breakfast time")
    if 12 <= hours <= 13:
        print("lunch time")
    if 18 <= hours <= 19:
        print("dinner time")


def convert(time):
    # splitting the time in hours and minute
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) / 60
    return hours + minutes


if __name__ == "__main__":
    main()
