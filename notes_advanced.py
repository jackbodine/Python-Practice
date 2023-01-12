import platform
import math
import json
import re
import os
import datetime as dt
import notes as n
from random import randint


# ---- Modules ----
# Modules are the same as a code-library. A file containing a set of functions that you want to use.
# This file imports notes, so we can use any function defined in that file.
def modules_example():
    n.default_parameter()
    print(n.moduleVariable)  # Can also access variables from the module.

    # The 'as' keyword renamed the module for the current file.

    # Python has several built in modules like platform.
    print(platform.system())
    # The dir() function lists all the function names from a module.
    print(dir(platform))

    # The 'from' keyword imports only certain parts of a module.
    print(randint(1, 10))


# ---- Dates ----
# noinspection SpellCheckingInspection
def dates_example():
    x = dt.datetime.now()  # returns a datetype object
    print(x)
    print(type(x))
    print(x.year)  # This works because x is an object with a year variable

    # You can create specific datetime objects as such:
    _ = dt.datetime(2000, 10, 6)

    # datetime has a method called strftime() which returns a readable string and takes a desired format
    print(x.strftime("%B %d, %Y"))


# ---- Math ----
def math_example():
    # the math module has myriad built-in functions
    x = math.sqrt(35)
    print(x)
    p = math.pi
    y = math.ceil(6.4)
    z = math.floor(1.2)


# ---- JSON ----
def json_example():
    # If you have a json string, you can use json.loads() to convert it into a python dictionary.
    x = '{ "name":"John", "age":30, "city":"New York"}'
    y = json.loads(x)
    print(y["age"])
    # json.dumps() goes in the reverse direction.
    x = json.dumps(y)
    x = json.dumps(y, indent=4, sort_keys=True)  # Puts proper indentation into the json string.


# ---- RegEx ----
def regex_example():
    txt = "The rain in Spain"
    txt2 = "hello"
    x = re.search("^The.*Spain$", txt)  # checks if the text starts with "The" and ends in "Spain", returns a match obj.
    print(x)  # x is a Match object,

    # .findall returns a list of all matches
    # x = re.findall("ai", txt)
    # print(x)

    if type(x) is not type(None):
        print("found a match")
    else:
        print("No Match")


# ---- Errors ----
def errors_example():
    try:
        print(x)
    except NameError:
        print("x is undefined. :(")
    except:
        print("Something else went wrong. :(")

    # Else statements are ran if nothing goes wrong.
    try:
        print("Hello")
    except:
        print("Something went wrong")
    else:
        print("Nothing went wrong")

    # Finally is run at the end of the block, regardless of if something went wrong.
    try:
        print(x)
    except:
        print("Error Occurred")
    finally:
        print("Block finished.")

    # The raise keyword is used to throw exceptions
    x = -1
    if x < 0:
        raise Exception("Sorry, no numbers below zero")


# ---- User input ----
def user_input_example():
    x = input("Enter username: ")
    print("Username is ", x)


# ---- Text formatting ----
def format_example():
    price = math.pi
    txt = "The price is {:.2f} dollars"  # Curly brackets in strings act as placeholders for format.
    print(txt.format(price))  # replaces the curley brackets with a variable.

    # formatted string literals (Also called f-strings)
    year = 2016
    event = "Election"
    str = f'Results of the {year} {event}'
    print(str)

    # {:int} wil cause a string to be a minimum of int characters long
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    for name, phone in table.items():
        print(f'{name:10} ==> {phone:10d}')


# ---- Files ----
def files_example():
    # the open() function is used for reading files.
    f = open("data.txt")  # with no extra parameters, the file is opened in read mode.
    input = f.read()  # turns the file content into a string.
    f.close()  # Good practice to close a file when you are done with it.

    print(input)

    # Deleting files
    # Use the os package.
    if os.path.exists("demofile.txt"):
        os.remove("demofile.txt")
    else:
        print("The file does not exist")


def match_example():
    # Added in python 3.10
    status = 404
    match status:
        case 400:
            print("Bad request")
        case 404:
            print("Not found")
        case 418:
            print("I am a teapot")
        case 416 | 417:  # or
            print("Not allowed")
        case _:
            print("Something else went wrong")


def positional_vs_keyword():
    # In notes.py we see that * can be used for optional parameters.
    # '/' denotes a positional only parameter.
    def positional_only(arg, /):
        pass
    # this function would throw an error


def walrus_operator():
    # Officially called the "assignment expression operator"
    if x := True:
        print(x)

    # According to some youtube videos this is a controversial operator.
    (x := 42) # 1. Assigns 42 to x, returns 42.

    # Example shortening:
    # Looks for a match, if it finds one, print.
    res = re.match(r"\w", "Hello")
    if res:
        print(res.group(0))

    # This becomes
    if res := re.match(r"\w", "Hello"):
        print(res.group(0))


if __name__ == '__main__':
    # modules_example()
    # dates_example()
    # math_example()
    # regex_example()
    # errors_example()
    # user_input_example()
    # format_example()
    # files_example()
    # match_example()
    walrus_operator()
