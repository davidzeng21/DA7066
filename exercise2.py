# 1. Which alternative/alternatives should you keep in mind when choosing identifiers for variables
# and functions?
# a) identifiers should be short
# b) identifiers should be descriptive
# c) identifiers should be unique within the function/module/program/script
# d) An identifiers should be written with capitals
# e) None of the above

# answer: b, c

# 2. Write code that read an integer from the user and prints “Odd” if it is an odd number and “Even” if
# the number is even.

def odd_even():
    try:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")
    except ValueError:
        print("Please enter a valid number")

odd_even()

# 3. Make truth tables for the boolean operators and and or (i.e., replace the question marks with True
# or False in the table below).

# a) and operator truth table (True and True = True, otherwise False)
# True and True = True
# True and False = False
# False and True = False
# False and False = False

# b) or operator truth table (False or False = False, otherwise True)
# True or True = True
# True or False = True
# False or True = True
# False or False = False

# 4. Try, without running the code, to evaluate these four expressions for all possible values of x, y
# and z:
# a) not x or not y
# b) x and (y or z)
# c) (x != z) and not y
# d) x and z

# answer:
# a) not x or not y
# True or True = True
# True or False = True
# False or True = True
# False or False = True

# b) x and (y or z)
# True and True = True
# True and False = False
# False and True = False
# False and False = False

# c) (x != z) and not y
# True and True = True
# True and False = False
# False and True = False
# False and False = False

# d) x and z
# True and True = True
# True and False = False
# False and True = False
# False and False = False

(not x) or (not y)
x and (y or z)
(x != z) and not y
x and z

# 5. Write a Python function that corresponds to the mathematical function f ¹x;yº = xy. We want
# the function to notify the user if a number other than 0 is divided by 0. In this case, the function
# should print out The result is infinite... but not return any explicit value. If 00 is called,
# the function should print Indeterminate form... and not return anything either.