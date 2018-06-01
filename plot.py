'''
A python script to compute bandgap in zinc oxide
Requires 1 argument in command line. 
Example, python compute_bandgap doscar
'''

import matplotlib.pyplot as plt 
import sys
import numpy as np

'''
Function to convert numbers in E+ and E- exponential format to 
normal floating point numbers. 
'''

def stringToFloat(myStr):
    if 'E+' in myStr:
        myStr=myStr.split('E+')
        return float(myStr[0])*pow(10,float(myStr[1]))
    elif 'E-' in myStr:
        myStr=myStr.split('E-')
        return float(myStr[0])* pow(10,float(myStr[1])*-1)
    else:
        return float(myStr)

doscarFile=open(sys.argv[1])
result=[] # List to keep the result
x_values=[]
y_values=[]
is_zero=False

'''
Reads each lines from the Doscar file, filtres out the lines with first column in the range -3 to 3. 
For each of these lines, finds the first occurance of 0 in the 2nd column
Appends the result until it finds the first occurance of non-zero. 
Appends the first first occurance of non-zero. 
The loop stops. 
'''
for lines in doscarFile:
    lines=lines.strip().split('  ')
    if stringToFloat(lines[0])>=-3 and stringToFloat(lines[0])<=3:
    	x_values.append(stringToFloat(lines[0]))
    	y_values.append(stringToFloat(lines[1]))
doscarFile.close()

print(x_values)
print(y_values)
plt.plot(x_values,y_values,'ro')

plt.axis([-3,3,0,400])

plt.show()
