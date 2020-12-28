#!/usr/bin/env python

import sys
from itertools import combinations
from itertools import combinations_with_replacement

class Number:
    def __init__(self):
        self.value = 0
        self.history = ""

    def printme(self):
        print("%d = %s" % (self.value, self.history))


def reduce(two_numbers):
    "Reduce two numbers to one"
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
    if b.value != 0:
        c = Number()
        c.value = a.value / b.value
        c.history = "(" + a.history + "/" + b.history + ")"
        results.append(c)

    # b / a
    if a.value != 0:
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


def solver(numbers):
    queue = [numbers]
    singles = []
    while queue:
        #print("Begining of loop, length of Q = %d" % len(queue))

        # pop a numbers object
        object = queue.pop(0)

        # pick two numbers from the object
        picked_list = combinations(object, 2)

        #print("Length of object: %d" % len(object))
        for picked in picked_list:
            the_rest = set(object) - set(picked)

            # reduce two numbers to one,
            reduced_list = reduce(picked)
            #print("Remaining=", len(the_rest))
            if len(the_rest) > 0:  # if the object has other member, put them together and append to the queue
                for reduced in reduced_list:
                    #print({reduced} | the_rest)
                    queue.append(list(the_rest | {reduced}))
                    #print(len(queue))
            else:   # else it is a single object now, put to singles
                for reduced in reduced_list:
                    singles.append(reduced)

        #print("End of loop, length of Q = %d" % len(queue))

    for x in singles:
        if x.value == 24:
            return x

    return None

if __name__ == "__main__":

    if len(sys.argv) > 2:
        numbers = []
        for x in sys.argv[1:]:
            n = Number()
            n.value = int(x)
            n.history = x
            numbers.append(n)

        solution = solver(numbers)
        if solution:
            solution.printme()
    else:  # investigate all
        all_numbers = combinations_with_replacement([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4)
        all_numbers = list(all_numbers)
        N_allcombos = len(all_numbers)
        Counter = 0
        for numbers_int in all_numbers:
            numbers = []
            for x in numbers_int:
                n = Number()
                n.value = x
                n.history = str(x)
                numbers.append(n)
            solution = solver(numbers)
            if solution:
                print("%s: " % str(numbers_int), end="")
                solution.printme()
                Counter += 1

        print("%d solutions out of %d combinations. Solvable rate = %.2f%%" % (Counter, N_allcombos, Counter/N_allcombos*100))


