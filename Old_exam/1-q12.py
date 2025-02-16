def substring_abundance(s, k):
    d = {}
    for i in range(len(s) - k + 1):
        substring = s[i:i+k]
        if substring not in d: # new entry
            d[substring] = 0
        d[substring] += 1
    return d

def most_abundant_substrings(s, k):
    max_count = 0
    most_frequent_substrings = {}
    d = substring_abundance(s, k)
    # find the largest count
    for count in d.values():
        if count > max_count:
            max_count = count
    # return the most frequent substring
    for substring, count in d.items():
        if count == max_count:
            most_frequent_substrings[substring] = count
    return most_frequent_substrings

print(most_abundant_substrings("AAA", 2))

print(most_abundant_substrings("ACGACGA", 3))