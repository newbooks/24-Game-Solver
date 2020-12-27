#!/usr/bin/env python

import sys


class Number:
    def __init__(self):
        self.value = 0
        self.history = ""

    def printme(self):
        print("My value is %d, and my history is %s" % (self.value, self.history))


def tryout2(two_numbers):
    results = []
    a = two_numbers[0]
    b = two_numbers[1]

    # a + b
    c = Number()
    c.value = a.value + b.value
    c.history = "(" + a.history + "+" + b.history + ")"    # output (2+3)
    results.append(c)

    # a - b
    c = Number()
    c.value = a.value - b.value
    c.history = "(" + a.history + "-" + b.history + ")"
    results.append(c)

    # b - a
    c = Number()
    c.value = b.value - a.value
    c.history = "(" + b.history + "-" + a.history + ")"
    results.append(c)

    # a * b
    c = Number()
    c.value = a.value * b.value
    c.history = "(" + a.history + "x" + b.history + ")"
    results.append(c)

    # a / b
    c = Number()
    c.value = a.value / b.value
    c.history = "(" + a.history + "/" + b.history + ")"
    results.append(c)

    # b / a
    c = Number()
    c.value = b.value / a.value
    c.history = "(" + b.history + "/" + a.history + ")"
    results.append(c)

    # Throw away negative values
    results = [x for x in results if x.value >= 0.0]

    # Merge redundant values
    values = []
    new_results = []
    for x in results:
        if x.value not in values:
            new_results.append(x)
            values.append(x.value)

    return new_results


def tryout3(three_numbers):
    results = []

    for i_exclude in range(3):
        two_numbers = []
        for j in range(3):
            if j != i_exclude:
                two_numbers.append(three_numbers[j])

        step1_results = tryout2(two_numbers)
        for x in step1_results:
            two_numbers = [x, three_numbers[i_exclude]]
            step2_results = tryout2(two_numbers)
            results = results + step2_results

    new_results = []
    appeared_values = []
    for x in results:
        if x.value not in appeared_values:
            new_results.append(x)
            appeared_values.append(x.value)

    return new_results


if __name__ == "__main__":

    numbers = []
    for x in sys.argv[1:]:
        n = Number()
        n.value = int(x)
        n.history = x
        numbers.append(n)
        # n.printme()

    # We have 3 numbers
    outcomes = tryout3(numbers[:3])
    for outcome in outcomes:
        print(outcome.value, "=", outcome.history)


    # We have two numbers
    # outcomes = tryout2(numbers[:2])
    #
    # for outcome in outcomes:
    #     print(outcome.value, "=", outcome.history)
