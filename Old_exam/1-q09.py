def contains_substring(lis, ss):
    sslis = []
    for s in lis:
        if ss in s:
            sslis.append(s)
    return sslis

print(contains_substring(['ab', 'cde'], 'de'))

print(contains_substring(['apple', 'strawberry', 'pear'], 'r'))