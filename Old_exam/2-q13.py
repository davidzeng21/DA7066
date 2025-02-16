def common_max(l1,l2):
    while True:
        if l1 == []:
            return 0
        m1 = max(l1)
        if m1 in l2:            
            return m1
        else:
            l1.remove(m1)

print(common_max([6,1,2,4],[2,3,5]))

print(common_max([6,1,2,3,4],[4,2,3,6,7]))

print(common_max([6,1,4],[2,3,5]))