import exercise5

x = 6
assert exercise5.is_perfect(x) == True, "6 Should be perfect"
x = -1
assert exercise5.is_perfect(x) == False, "-1 is not perfect"

# decide how your program should behave for wrong data type
x = '91'
try:
    exercise5.is_perfect(x)
    assert False, "is_perfect did not throw TypeError for string"
except TypeError:
    pass # worked fine, we want a type error
# some more tests on is_prime

x = 2
assert exercise5.is_prime(x) == True, "2 is prime"