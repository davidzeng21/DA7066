def construct_dict():
    d = {}
    while True:
        key = input('Provide key: ')
        if key == 'quit':
            break
        elif key in d:
            print('The key is already in the dictionary.')
            continue
        else:
            value = input('Provide value:')
            d[key] = value

    return d

d = construct_dict()
print(d)