import sys
import glob

print('argv',sys.argv[1])
for filename in glob.glob(sys.argv[1]):
    print('filename',filename)
    with open(filename,'r') as infile:
        a = b = c = 0
        for line in infile.readlines():
            a += 1
            b += len(line.split())
            c += len(line)
        print(a,b,c,filename)
