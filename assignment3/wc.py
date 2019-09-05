import sys

for filename in sys.argv[1:]:
    with open(filename,'r') as infile:
        a = b = c = 0
        for line in infile.readlines():
            a += 1
            b += len(line.split())
            c += len(line)
        print('{:3d} {:3d} {:3d} {}'.format(a,b,c,filename))
