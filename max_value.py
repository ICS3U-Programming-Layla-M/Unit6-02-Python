#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: June 11, 2021
# This program generates 10 random numbers into an array/list between 0 and
# 100 and displays the number with the highest value

import constants
import random


def find_max_value(array):
    # checks for the highest value/number in a list/array
    counter = constants.MIN_NUM
    max = array[counter]

    for counter in range(constants.MIN_NUM, len(array)):
        if (array[counter] > max):
            max = array[counter]
        else:
            max = max
        counter = counter + 1
    return max


def main():
    # create an empty list
    number_array = []

    for counter in range(constants.MIN_NUM, constants.MAX_ARRAY_SIZE):
        # generate random number from 0 to 100 and add it to the list
        random_number = random.randint(constants.MIN_NUM, constants.MAX_NUM)
        number_array.append(random_number)

        # display the random number added and at which position/index
        print("{0} added to the list at position {1}.\
". format(random_number, counter))
        counter = counter + 1
    print()

    # call function to check for the highest value in the array
    max_value = find_max_value(number_array)

    # display the highest value in the array
    print("The maximum value is: {}". format(max_value))
    print()


if __name__ == "__main__":
    main()
