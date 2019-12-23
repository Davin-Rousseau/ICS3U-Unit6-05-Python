#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Dec 2019
# This program uses a list


def average_marks(marks):
    # this function calculates average of marks
    # in the list
    total = 0
    counter = 0
    for counter in marks:
        total = total + counter
        counter += 1
    average = total / len(marks)

    return average


def main():
    # this function uses a list

    marks = []
    single_mark = None
    counter = 0

    # input
    print("Please enter a mark from 0-100 at a time. Enter -1 to end.")

    try:
        while single_mark != -1:
            single_mark = int(input("Enter a mark: "))
            counter += 1
            marks.append(single_mark)
        marks.pop()  # remove the -1 that was added
        average = average_marks(marks)
        print("")
        print("The average of the given marks is: {0:,.2f}".format(average))
    except ValueError:
        print("Invalid input")


if __name__ == "__main__":
    main()
