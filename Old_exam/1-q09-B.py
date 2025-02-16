def contains_substring(lis, ss):
    sslis = []
    for i in range(len(lis)):
        try:
            if ss in lis[i]:
                sslis.append(lis[i])
        except:
            print("invalid datatype at index:", i)
    return sslis

print(contains_substring(['ab', 'cde', 2, True], 'de'))

print(contains_substring([False, 'apple', 'strawberry', 'pear', 3.14], 'r'))