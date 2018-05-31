'''
A python script to compute bandgap in zinc oxide
'''

import sys

def stringToFloat(myStr):
    print(myStr)
    if 'E+' in myStr:
        myStr=myStr.split('E+')
        return float(myStr[0])*pow(10,float(myStr[1]))
    else:
        myStr=myStr.split('E-')
        return float(myStr[0])* pow(10,float(myStr[1])*-1)

doscarFile=open(sys.argv[1])

for lines in doscarFile:
    lines=lines.strip().split('  ')
    if float(lines[0])>=-3 and float(lines[0])<=3:
        
        print(stringToFloat(lines[1]))

doscarFile.close()
