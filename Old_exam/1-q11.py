def substring_abundance(s, k):
    d = {}
    for i in range(len(s) - k + 1):
        substring = s[i:i+k]
        if substring not in d: # new entry
            d[substring] = 0
        d[substring] += 1
    return d

# Expected output: {'AA': 2, 'AA': 1}
print(substring_abundance("AAA", 2))
# Expected output: {'ACG': 2, 'CGA': 1, 'GAC': 1}
print(substring_abundance("ACGACGA", 3))