import sys
import random
i = 0
while True:
    n = random.randint(0,1000000)
    try:
        res = i / n
    except ZeroDivisionError:
        print('Warning: Tried divide {0} with 0.'.format(i), file=sys.stderr)
    if i % 1000000 == 0:
        print('Progress {0} million iterations.'.format(i), file=sys.stdout)
    i+=1