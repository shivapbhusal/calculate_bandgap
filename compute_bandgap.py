'''
A python script to compute bandgap in zinc oxide
'''

import sys

doscarFile=open(sys.argv[1])

for lines in doscarFile:
    lines=lines.strip().split('  ')
    print(lines)

doscarFile.close()
