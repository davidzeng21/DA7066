def rev(s):
    s_rev = ''
    if s == '':
        raise ValueError("rev: input string is empty")
    s_rev = s[::-1]
    return s_rev

print(rev("hubba"))
print(rev("foo"))

try:
    print(rev(""))
except ValueError as e:
    print(f"{e}: Correctly raised value error")