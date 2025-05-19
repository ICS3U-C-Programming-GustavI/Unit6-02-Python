#!/usr/bin/env python3
# Created by: Gustav I
# Created on: April 19, 2025
# This program generates 10 random numbers, stores them in a list,
# and uses a function to find and return the max value.

import random

# Constants
MAX_ARRAY_SIZE = 10
MIN_NUM = 0
MAX_NUM = 100


# Function to find the biggest value of the list returned to user
def find_max_value(numbers):
    max_val = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > max_val:
            max_val = numbers[i]
    return max_val


def main():
    list_of_int = []

    print("=== Max Value Finder ===")
    print("Generating random numbers...\n")
    # Loop through the list and add number to array/list
    for _ in range(MAX_ARRAY_SIZE):
        num = random.randint(MIN_NUM, MAX_NUM)
        list_of_int.append(num)
        print(f"{num} added to the list!")
    # Print all the numbers and the list
    print("\nAll numbers added!")
    print("List of numbers:", list_of_int)
    # Print the max value
    max_value = find_max_value(list_of_int)
    print(f"\nThe max value is: {max_value}")


# Call the main function
if __name__ == "__main__":
    main()
