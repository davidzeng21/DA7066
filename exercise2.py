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

# 5. Write a Python function that corresponds to the mathematical function f (x,y) = x/y. We want
# the function to notify the user if a number other than 0 is divided by 0. In this case, the function
# should print out The result is infinite... but not return any explicit value. If 0/0 is called,
# the function should print Indeterminate form... and not return anything either.

def divide(x, y):
    """
    This function performs division of x by y.
    
    If x is not 0 and y is 0, it prints 'The result is infinite...'.
    If both x and y are 0, it prints 'Indeterminate form...'.
    Otherwise, it prints the result of the division.
            print(f"{x/y}")
    """
    if x != 0 and y == 0:
        print('The result is infinite...')
    elif x == 0 and y == 0:
        print('Indeterminate form...')
    else:
        print(f"{x/y}")


# 6. Let:

x = True
y = False

# Which expressions below evaluate to True? Why?
(x and y) or (not x and not y)
# (True and False) or (not True and not False)
# False or (False and True)
# False or False
# False

(x or y) and (not x or not y)
# (True or False) and (not True or not False)
# (True) and (True)
# True

x or y or not x or not y
# True or False or not True or not False
# True or False or False or True
# True

not(not x and not (x and y))
# not(not True and not (True and False))
# not(False and not False)
# not(False and True)
# not(False)
# True

# 7. Define nand, nor, and xnor as Python functions.

def nand(x, y):
    """
    This function performs NAND operation on x and y.
    """
    return not(x and y)

def nor(x, y):
    """
    This function performs NOR operation on x and y.
    """
    return not(x or y)

def xnor(x, y):
    """
    This function performs XNOR operation on x and y.
    """
    return x == y

# 8. Test the functions nand, nor, and xnor with arguments that are not of the type bool. Are the
# results what you expected? If not, why?

print(nand(1, 0)) 
print(nand(0, 1)) 
print(nand(1, 1)) 
print(nand(0, 0)) 

print(nor(1, 0)) 
print(nor(0, 1)) 
print(nor(1, 1)) 
print(nor(0, 0)) 

print(xnor(1, 0)) 
print(xnor(0, 1)) 
print(xnor(1, 1)) 
print(xnor(0, 0))