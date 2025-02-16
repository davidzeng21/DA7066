i = 1
def rev(s):
    global i
    s_rev = ''
    while True:
        if i <= len(s):
            s_rev += s[-i]
            i += 1
        else:
            break
    return s_rev

def rev(s):
    i = 1
    s_rev = ''
    for i in range(1, len(s)+1):
        s_rev += s[-i]
        i += 1

    return s_rev

print(rev('hubba'))