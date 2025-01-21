# 1. What happens if we run the code below? Why?
x,y = 2,3
x,y = y,x
print(x)
print(y)

# 2. Below is code to define the variables x and y with assigned values. Create and print a variable z with the value 100 by combining x and y arithmetically.

x,y = 4, -3
z=100*(x+y)
print(z)

# 3. Write code to print 'hejhejhejhejhejhejhejhejhejhejhejhejhejhejhejhej' (i.e., sixteen
#copies of hej).
s = 'hej'
16*s

# 4. Write code that results in 'hejhejhejhejhejhejhejhejhejhejhejhejhejhejhejhej' by using
# the + operator as few times as possible.
s = 'hej'

# 5. Write code that asks the user for first and last name, stores them in variables, and then prints a
# greeting. Look at the section section 1.6 above for inspiration.
first_name = input('What is your first name?')
last_name = input('What is your last name?')
print('Hi', first_name, last_name,'!')

# 6. Write code that asks the user for his/her age and favorite number and store them in two variables.
#What happens if you add those values and prints the result? What did you expect and what can
#you conclude about age and num?

age = int(input('What is your age?'))
num = int(input('What is your favorite number?'))
print(age+num)

