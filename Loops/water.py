# while loop


# from soil import sample
from pickle import TRUE
import random


def sample_moisture():
    return random.randint(18, 30)


# def main():
#     moisture = sample_moisture()
#     days = 0
#     print(f"{days}: Moisture is {moisture}%")

#     while moisture > 20:
#         moisture = sample_moisture()
#         days += 1
#         print(f"Day {days}: Moisture is {moisture}%")


def main():  # optimized code
    days = 0
    while TRUE:
        moisture = sample_moisture()
        print(f"day {days}: Moisture is {moisture}")
        days += 1
        if moisture < 20:
            break

    print("Time to water the plant")


main()
