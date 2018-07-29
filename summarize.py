import sys, os
f = open(sys.argv[1], 'r')
lines = f.readlines()
f.close()
lists = [float(line.split()[-1]) for line in lines]
print(sum(lists) / len(lists))