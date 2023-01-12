import random

moduleVariable = 4


### Iterators ###
# An iterator is an object that contains a countable number of values
# An interator is an object which implements the iterator protocol, the methods __iter__() and __next__()
# Iterators are different from iterable objects,
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

# We can create an iterable class ourselves.
class MyNumbers:
    def __iter__(self):  # can perform operations but must return the iterable object itself.
        self.a = 1
        return self

    def __next__(self):  # can also perform operations but must return the next object in the sequence.
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration  # Stops the iteration


def iterator_example():
    mytuple = ("apple", "banana", "cherry")
    myit = iter(mytuple)

    print(next(myit))  # next() returns an interator from an iterable container.
    print(next(myit))
    print(next(myit))

    for x in mytuple:  # for-loops loop through an iterable object
        print(x)  # The for loop actually creates an iterator object and executes the next() method for each loop.

    myclass = MyNumbers()
    myiter = iter(myclass)

    print(next(myiter))
    print(next(myiter))
    print(next(myiter))


### Classes ###
class MyClass:
    x = 5


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

    def introduce(self):
        print("Hello my name is " + self.name)


class Student(Person):  # Inherits the parent class.
    def __init__(self, name, age, year):
        super().__init__(name, age)  # Calls the parent's init()
        self.graduationYear = year


def class_example():
    p1 = MyClass()
    print(p1.x)

    p2 = Person("John", 36)
    print(p2.name)
    print(p2.age)
    p2.introduce()

    # You can modify the values of class variables without special methods
    p2.name = "Brad"

    # Use del to delete objects
    del p2  # RIP

    # Since classes can not be empty, you can use the pass keyword to compile. This also works elsewhere.
    try:
        pass
    except:
        pass


def inheritance_example():
    x = Student("Mike", 22, 2023)


### Casting ###
def casting_example():
    x = str(3)  # x will be '3'
    y = int(3)  # y will be 3
    z = float(3)  # z will be 3.0

    # type(x) returns the type of variable x.
    print(type(x))
    print("y is a " + str(type(y)))


### Variables ###
# Variables are case-sensitive a and A
# Starting a str with " or ' does not make a difference.
def variables_example():
    # You can assign multiple variables on the same line or multiple variables at once.
    x, y, z = "Orange", "Banana", "Cherry"
    x = y = z = "Orange"
    print(x + " " + y + " " + z)
    y = "Pineapple"
    print(x + " " + y + " " + z)

    # Unpacking a collection, works for list, tuples, etc.
    # Gives a ValueError: too many/not enough values to unpack if there aren't enough variables.
    fruits = ["apple", "banana", "cherry"]
    x, y, z = fruits
    print(x + " " + y + " " + z)


def output_variables_example():
    x = "Hello"
    y = "Hi"
    z = "Goodbye"
    print(x)

    # Variables can be chained with commas or pluses.
    # Pluses act as the mathematical operator for numbers
    print(x, y, z)
    print(x + y + z)


# Global variables are declared outside the scope of any function
gv = "awesome"


def global_variables():
    print("Python is " + gv)
    global gv2
    gv2 = "tubular"


### Data Types ###
def data_type_example():
    # Python has 15 different built in data-types
    # Text type: str
    myString = "Hello World"
    # Numeric type: int, float, complex
    # Note that Python does not have Doubles, only floats
    myInt = 20
    myFloat = 20.5
    myComplex = 1j
    # Sequence types: list, tuple, range
    myList = ["apple", "banana", "cherry"]
    myTuple = ("apple", "banana", "cherry")
    myRange = range(6)
    # Mapping types: dict
    myDict = {
        "A": "Hello",
        "B": "Goodbye"
    }
    # Set types: set, frozenset
    mySet = {"apple", "banana", "cherry"}
    myFrozenSet = frozenset({"apple", "banana", "cherry"})
    # Boolean type: bool
    myBool = True
    # Binary types: bytes, bytearray, memoryview
    myBytes = b"Hello"
    myByteArray = bytearray(5)
    myMemoryView = memoryview(bytes(5))
    # NoneType: NoneType
    myNone = None


### Numbers ###
def numbers_exmaple():
    int = 5
    float = -5.0
    float = 4e29
    complex = 4 + 2j

    r = random.randrange(1, 10)  # gets a number between 1 and 9.


### Strings ###
def strings_example():
    # Double quotes and single quotes are the same.
    a = "Hello"
    multilineString = """Line 1
    Line 2
    Line 3."""

    # Strings are arrays and can be indexed.
    a = "Hello"
    print(a[0], a[4])
    for i in a:
        print(i)

    # Use len(x) to get the length.
    print(len(a))

    # Use in to check if a substring exists
    if "jack" in "jackson":
        print("Yes!")
    elif "jack" not in "jackson":
        print("No!")

    # use + to concat strings.
    a = "Hello, "
    b = "World"
    c = a + b

    # format() method.
    age = 36
    name = "My name is John and I am {}"
    print(txt.format(age))  # Turns age into a string to be printed.

    quantity = 3
    itemno = 567
    price = 49.95
    myorder = "I want {} pieces of item {} for {} dollars."
    print(myorder.format(quantity, itemno, price))

    # Use a backslash to escape illegal characters
    txt = "We are the so-called \"Vikings\" from the north."
    # \n for new line, \t for tab, \b for backspace, \

    # There are many string methods, they return a string and do not change the original string.
    txt = "Fear is the mind killer."
    print(txt.capitalize())
    print(txt.zfill(3))


def booleans():
    # bool() allows you to check if certain values are empty
    print(bool([1]))
    print(bool([]))

    # the following return false
    bool(False)
    bool(None)
    bool(0)
    bool("")
    bool(())
    bool([])
    bool({})
    # This happens when an objects __len__() method returns false.

    # Other built in python functions like isinstance return booleans.
    x = 5
    print(isinstance(x, int))


def operators():
    # python has the standard arithmatic operators
    x = 5 ** 5  # 5^5
    x = 5 % 5
    x = 9 // 5  # floor division

    # An operator can become an assignment operator by adding an equal sign


def lists():
    # lists in python can contain different types
    myList = [1, "hello", True, 63j]
    myList = list((1, "hello", True, 63j))
    # lists are one of 4 collections built into python, the others are: set, tuple, and dictionary.

    # list can be indexed in reverse
    print(myList[-1])  # prints the last time in the list, 63j
    if 63j in myList:
        print("63j exists in list")

    # You can change multiple items in a list at once.
    myList[1:3] = ["Goodbye", False, "the last value is not included"]
    myList[1:4] = ["This removes several items"]

    # Items can be inserted in at specific index
    myList.insert(2, "Hello")
    myList.insert(10, "Sup")  # This is put at the end of the list.

    print(myList)

    # List can be extended by any iterable using .extend
    myTuple = (1, 3, 4)
    myList.extend(myTuple)

    # Removing items
    # Specific items can be removed using .remove
    myList.remove("Sup")
    # .pop removes items at a certain index
    myList.pop(3)
    myList.pop()  # removes the last item
    myList.clear()  # removes all items

    thisList = ["A", "B", "C", "D"]
    for i in range(len(thisList)):
        print(thisList[i])


def list_comprehension():
    myList = [str(x) for x in range(5)]
    fruits = ["Apple", "Banana", "Pear", "Kiwi", "Coconut"]
    aFruits = [x for x in fruits if "a" in x]  # List of fruits with the letter 'a'
    # newlist = [expression for item in iterable if condition == True]
    smallNumbers = [x for x in range(10) if x < 5]
    newlist = [x.upper() for x in fruits]  # the expression can be operated on.


def more_lists():
    # Lists have a .sort() function
    letters = ["x", "k", "b", "e"]
    letters.sort()
    letters.sort(reverse=True)

    # sorts can use custom functions
    def myfunc(n):
        return abs(n - 50)

    thislist = [100, 50, 65, 82, 23]
    thislist.sort(key=myfunc)
    print(thislist)

    # sorting alphabetically is case-sensitive, changing the key function can get around this.
    thislist = ["banana", "Orange", "Kiwi", "cherry"]
    thislist.sort(key=str.lower)
    print(thislist)

    # lists can be reversed with .reverse
    thislist.reverse()
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]

    # Aside from .extend, you can append lists using +
    list3 = list1 + list2


def tuples():
    # tuples are unchangeable, ordered and allow duplicate
    myTuple = (1, 2, 3)
    len(myTuple)

    # To create a tuple with one item, you need a common for python to recognize it.
    singleTuple = ("Hello",)

    tuple1 = ("abc", 34, True, 40, "male")
    thistuple = tuple(("apple", "banana", "cherry"))

    # tuples are indexed similar to lists.
    print(tuple1[2])

    # tuples are immutable, but you can convert them to lists, change the list then convert back to tuple
    x = ("apple", "banana", "cherry")
    y = list(x)
    y[1] = "kiwi"
    x = tuple(y)

    # Unpacking a tuple
    fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
    (green, tropic, *red) = fruits  # red becomes a list of all remaining
    (green, *tropic, red) = fruits  # tropic becomes a list of all extra items


def sets():
    # sets are unordered, unindexed and the items cannot be changed.
    thisset = {"apple", "banana", "cherry"}

    # You cannot index sets, instead you can iterate through them.
    for x in thisset:
        print(x)

    thisset.add("orange")
    print(thisset)
    tropical = {"pineapple", "mango", "papaya"}
    thisset.update(tropical)  # adds any iterable to set, similar to .extend for lists.
    thatset = {"red", "green", "blue"}
    thisset.union(thatset)  # similar to .extend but only for sets.
    print(thisset)

    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    set3 = set1.intersection(set2)  # takes the intersection of two sets.
    set4 = set1.symmetric_difference(set2)  # inverse of an intersection {1,2,5,6}

    # You can use .remove() or .discard() to remove items in a set.
    # The difference is that .discard() won't throw an error if the item doesn't exist in the set.
    thisset.remove("pineapple")
    thisset.discard("pineapple")


def dictionary_example():
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print(thisdict)

    # Accessing values in a dict
    carBrand = thisdict["brand"]
    carModel = thisdict["model"]
    # These are identical to the dict.get() method.
    carBrand = thisdict.get("brand")
    carModel = thisdict.get("model")

    # Prints the number of key/value pairs in a dictionary
    print(len(thisdict))

    # Keys can be of any type:
    thisdict = {
        "brand": "Ford",
        "electric": False,
        "year": 1964,
        "colors": ["red", "white", "blue"]
    }

    # x becomes a 'view' of the dictionary, it is a list of keys that will automatically update if the dict does
    x = thisdict.keys()
    # .values() works the same way.
    y = thisdict.values()
    # .items() returns all pairs in a dictionary in a list of tuples. It too is a view
    z = thisdict.items()

    # you can check if a key exists using the in keyword
    if "brand" in thisdict:
        print("Yes, 'brand' is one of the keys in thisdict")

    # items can easily be updated by referring to their name
    thisdict["year"] = 1985
    thisdict.update({"year": 1985})  # .update takes a second dictionary and modifies the first.
    # adding items is done by referencing keys that don't exist.
    thisdict["owner"] = "Jeff"
    print(thisdict)

    # .pop removes a pair
    thisdict.pop("colors")
    del thisdict["owner"]  # del also works

    # thisdict.clear() empties the entire dictionary

    for x in thisdict:  # iterating through keys
        print(x)

    for x in thisdict:  # iterating through values
        print(thisdict[x])

    for x, y in thisdict.items():  # iterates through pairs
        print(x, y)

    # using dict1 = dict2 only creates a reference to dict2. Use .copy() to duplicate dicts.

    # A dictionary can contain dictionaries, this is called nested dictionaries.


def control_flow():
    # Shorthand if
    a, b = 3, 4
    if a < b: print("3 is less than 4")  # These are generally discouraged by PEP8

    # like most languages, loops have break and continue keywords

    for x in range(3):  # prints 0, 1, 2.
        print(x)

    for x in range(0, 10, 3):  # increments by 3
        pass

    # for loops can have else statements to run once the loop finishes

    for x in []:
        print(x)
    else:
        print("finished")  # Will run even if the for loop never runs.


def slicing_strings_example():
    string = "Hello World"
    print(string[2:5])
    print(string[:5])
    print(string[4:])
    # Negative indexing
    print(string[-5:-2])


def modifying_strings():
    a = "Hello, World"
    print(a.upper())
    print(a.lower())
    print(a.strip())  # removes whitespace
    print(a.replace("l", "k"))  # replaces all "l"s with "k"s
    list = a.split(",")  # returns ['Hello', ' World!']


# ----- FUNCTIONS -----
# lists can be passed as arguments

def arbitrary_args(*kids):
    # function receives a tuple of arguments.
    print("The youngest child is " + kids[2])


def keyword_args(first, second, third):
    # functions are called like: keyword_args(first = "A", third = "C", second = "B")
    print(first, second, third)


def arbitrary_keyword_args(**values):
    # Similar to arbitrary_args but recieves a dictionary of keyword arguments instead of a list.
    # Called like arbitrary_keyword_args(first = "A", third = "C", second = "B"), just like keyword arguments
    pass


def default_parameter(country="Denmark"):
    print("I am from ", country)
    # will use the default value unless another is specified when called.


def lambda_example():
    # A lambda function is a small unnamed function. It can take any number of arguments but only have one expression.
    # lambda arguments : expression

    x = lambda a: a + 10
    print(type(x))  # x is a function! It takes a variable and adds 10.
    print(x(5))  # prints 15!

    x = lambda a, b: a * b
    print(x(5, 6))

    # lambdas are useful when you need to have your code make functions while running.
    # For example, you need a function that multiplies a number by n, where n is determined at runtime.
    def myfunc(n):  # Creates and returns a function that multiples a number by n.
        return lambda a: a * n

    mydoubler = myfunc(2)  # creates a function that multiples a number by 2.
    print(mydoubler(11))  # uses the new function.

    # Use lambda functions when an anonymous function is required for a short period of time


if __name__ == '__main__':
    print("Test Doc.")
    # Variables
    # casting_example()
    # variables_example()
    # output_variables_example()
    # global_variables()

    # Data Types
    # data_type_example()
    # class_example()

    # iterator_example()
    # lists()
    # sets()
    # dictionary_example()
    # control_flow()
    # arbitrary_args("Emil", "Tobias", "Linus")
    lambda_example()
