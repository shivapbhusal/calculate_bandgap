'''
A python script to compute bandgap in zinc oxide
Requires 1 argument in command line: doscar file. 
Example, python compute_bandgap doscar 0 10

Created by: Shiva Bhusal, Aneer Lamichhane. 
'''

import sys

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
seriesList=[] # List to keep the series of values in each Gaps.
is_zero=False

'''
Reads each lines from the Doscar file, filtres out the lines with first column in the range -3 to 3. 
For each of these lines, finds the first occurance of 0 in the 2nd column
Appends the result until it finds the first occurance of non-zero. 
Appends the first first occurance of non-zero. 
The loop stops. 
'''
tempSeries=[]
for lines in doscarFile:
    lines=lines.strip().split('  ') # Two spaces.
    if stringToFloat(lines[1])==0:
        tempSeries.append([stringToFloat(lines[0]),stringToFloat(lines[1])])
        is_zero=True
    if is_zero==True:
        if stringToFloat(lines[1])!=0:
            tempSeries.append([stringToFloat(lines[0]),stringToFloat(lines[1])])
            seriesList.append(tempSeries)
            tempSeries=[]
            is_zero=False

doscarFile.close()

print("Total Gaps:" +str(len(seriesList)))

gapList=[]
for series in seriesList:
    start=series[0][0]
    end=series[len(series)-1][0]
    gapList.append(end-start)

print(gapList)

