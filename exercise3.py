# 1. What is the result of [1,2] + ['a', 'b']?
[1,2] + ['a', 'b']

# 2. What happens if we use min/max on lists with elements of different types?
min([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])
# It will raise an error because the elements are not comparable between instances of 'str' and 'int'

# 3. Complete the function that takes in a string s and returns its vowels.
def vowels(s):
    vs = "AEIOUYaeiouy"
    out = ""
    for c in s:
        if c in vs:
            out += c

    return out

vowels("Hello World")

# 4. Modify the function in exercise 3 so that it instead returns the consonants in s, but do so without
# changing the string vs. Then write a function vowels_or_consonants taking an extra parameter
# that determines whether vowels or consonants should be returned. The parameter should have
# a default value so that vowels are returned if the programmer calls the function with only one
# argument.


def vowels_1(s):
    vs = "AEIOUYaeiouy"
    out = ""
    for c in s:
        if c not in vs and c != " ":
            out += c

    return out

vowels_1("Hello World")

def vowels_or_consonants(s, vowels=True):
    if vowels:
        return vowels(s)
    else:
        return vowels_1(s)
    

vowels_or_consonants("Hello World", False)



# 5. What happens if you leave out the code block beginning with if term != "" in the function
# split(s) above? Find an example of a string s such that the output is incorrect if it is missing.


def split(s,sep = " "):
    res = []
    term = ""
    for c in s:
        if c in sep:
            res.append(term)
            term = ""
        else:
            term += c

    # if term != "":
    #    res.append(term)

    return res

split("Hello World")

# The output will be ['Hello'] instead of ['Hello', 'World'] if the code block `term != ""` is missing

# Furthermore, how does split behave on strings with several spaces in a row? Write a correct
# version of the function.
split("Hello    World")
# The output will be ['Hello', '', '', ''] 

def split_1(s,sep = " "):
    res = []
    term = ""
    for c in s:
        if c in sep:
            if term != "":
                res.append(term)
            term = ""
        else:
            term += c

    if term != "":
        res.append(term)

    return res

split_1("Hello    World")

# 6. Test the following code snippet:

list = [1,2,3]
list2 = list
list2.reverse()
print(list)

# Does it work as you expected? Why not? How can you fix it?
# The output will be [3,2,1] instead of [1,2,3] because list2 is a reference to list. 
# To fix it, we can use the copy method to create a new list.

list = [1,2,3]
list2 = list.copy()
list2.reverse()
print(list)

# 7. Rewrite the code so that the list mylist is not empty at the end.
mylist = ["Ho","ho","ho!"]
mylist1 = mylist.copy()
while mylist1:
    x = mylist1.pop()
    print(x)
print(mylist)

# Tip: use .copy(). How can you do it without using copy?

mylist = ["Ho","ho","ho!"]
mylist1 = mylist[:]
while mylist1:
    x = mylist1.pop()
    print(x)
print(mylist)

for s in mylist:
    print(s)
print(mylist)

# 8. Try using continue, break and pass in the while loop below. What happens?
n = 10
while n > 0:
    n -= 1
    if n == 7:
        # test continue, break or pass here
        pass
    print(n)

# pass will do nothing and continue will skip the rest of the code block and go to the next iteration.
# break will stop the loop.

# 9. Write a while loop that reads in numbers from the user and saves them in a list. It should continue
#to read in until the user enters 0; then the program should end the loop and print out the list.

nums = []

while True:
    num = float(input("Enter a number: "))
    if int(num) == 0:
        nums.append(0)
        print(nums)
        break
    else:
        nums.append(num)

# 10. Write the function that calculates the GCD of a and b by testing all numbers between 1 and min(a,b) to see 
# which is the biggest number that divides both.
def naiveGCD(a,b):
    for gcd in range(min(a,b),0,-1):
        if a % gcd == 0 and b % gcd == 0:
            return gcd

naiveGCD(12,24)

# 11. Write the function passcode() that reads in one digit (1–9) at a time from the user. After each
# digit is read, the function should test if the last four digits entered matches the correct code. If the
# correct code is entered, the function should print Door unlocked! and return True. Choose the
# correct passcode yourself, for example 1337.
# if the user enters the wrong code, the function should continue to read in digits until the correct
# code is entered.
def passcode():
    code = "1337"
    passcode = ""
    while True:
        digit = input("Enter a digit: ")
        passcode += digit
        if len(passcode) > 4:
            passcode = passcode[1:]
        if passcode == code:
            print("Door unlocked!")
            return True


passcode()