import sys

f = open(sys.argv[1])

for l in f:
    if "the" in l:
        print(l)
        break
