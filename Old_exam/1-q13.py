def read_number():
    lst = []
    while True:
        ans = input('Enter a number: ')
        if ans == 'quit':
            break
        try:
            num = int(ans)
        except ValueError:
            print('Invalid number, please try again.')
            continue
        if num in lst:
            print('The number exists.')
            continue
        else:
            lst.append(num)
    return lst

lst = read_number()
print(lst)