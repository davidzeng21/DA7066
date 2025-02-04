pi = 3.14

def area(radius):
    return pi * (radius ** 2)

def circumference(radius):
    return 2 * pi * radius


def main():
    print("Circle tests")
    print("Pi is in this module set to:", pi)
    print("Area for 2 is:", area(2))
    print("Area for 5 is:", area(5))
    print("Circumference for 1 is:", circumference(1))
    print("Circumference for 2 is:", circumference(2))

if __name__ == '__main__':
    main()