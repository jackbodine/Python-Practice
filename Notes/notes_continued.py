from collections import deque
import os
import shutil

def backwards_range():
    for i in range(10, 0, -1):  # Counting backwards with Range
        print(i)


def function_annotations(name: str, age: int) -> str:
    return f"{name} is {age} years old."


def using_lists_as_stacks():
    # use .append() and .pop() to make a list act as a stack.
    stack = [1, 3, 5]
    print(stack.pop())
    stack.append(7)


def using_lists_as_queues():
    # Using a list as a queue is SLOW because adding/popping from the front
    # of a list makes the whole list shift by one.
    # Use deque from collections instead.
    queue = deque(["Eric", "John", "Mike"])
    queue.append("Gary")
    queue.append("Mort")
    print(queue.popleft())
    print(queue.popleft())
    print(queue)


def list_comprehension():
    squares = list(map(lambda x: x ** 2, range(10)))
    # Use the following method for better readability
    squares = [x ** 2 for x in range(10)]


def looping_techniques():
    # The following is an example for looping dictionaries.
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k, v in knights.items():
        print(f"Key: {k}, Value: {v}")

    # The following in an example of looping through an iterable with an index
    t = ["tic", "tac", "toe"]
    for i, v in enumerate(t):
        print(f"i: {i}, v: {v}")

    # Lists can be looped in reverse using reversed()
    for v in reversed(t):
        print(v)

    # Example of looping though two things at the same time,
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print(f"What is your {q}? It is {a}")

    print(zip(questions, answers))  # Prints <zip object>

    # Remember that you can convert lists to sets to remove duplicates.
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for i in sorted(set(basket)):
        print(i)


# Packages vs. Modules
# A MODULE is something you import at the beginning of a file.
# A PACKAGE is a collection of modules.
# Ex 'A.B' Means submodule B in package A.
# NumPy or Pillow are Packages.

# repr() vs. str()
# str(x) is meant to return a human-readable version of x
# repr(x) is meant to return interpreter-readable versions of x
# In many cases the output is the same.

def std_library():
    # The 'os' module provides functions for interacting with the OS.
    # print(dir(os))
    # 'shutil' provides a smaller number of functions for file management.
    # print(dir(shutil))
    # the 'glob' module finds path names to files that match unix patterns.
    # 'sys' provides access to command line arguments and interpreter info.
    # 'argparse' is a more robust module for command line arguments
    # 'math' provides access to math tools
    # 'random' provides access to rng
    # 're' -> regex
    # 'statistics' -> mean, median, variance
    # 'smtplib' -> emails?
    # 'datetime' -> time and dates
    # 'timeit' -> performance measurement
    # 'unittest' and 'doctest' write tests for projects

    pass


if __name__ == '__main__':
    #backwards_range()
    #looping_techniques()
    std_library()
