'''
A python script to compute bandgap in zinc oxide
Requires 1 argument in command line: doscar file. 
Example, python compute_bandgap doscar

File should be in three column format. Each of the columns are separated by two spaces. 
Make necessary modifications in the script if your file is different.

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
lineCount=0
tempSeries=[]
for lines in doscarFile:
    lineCount=lineCount+1
    try:
        fieldValues=lines.strip().split('  ') # Two spaces. Modify this if your file is different.
        if stringToFloat(fieldValues[1])==0:
            tempSeries.append([stringToFloat(fieldValues[0]),stringToFloat(fieldValues[1])])
            is_zero=True
        if is_zero==True:
            if stringToFloat(fieldValues[1])!=0:
                tempSeries.append([stringToFloat(fieldValues[0]),stringToFloat(fieldValues[1])])
                seriesList.append(tempSeries)
                tempSeries=[]
                is_zero=False
    except (IndexError,ValueError,TypeError):
        print("Line No "+str(lineCount)+" ignored")
        print("Formatting issues detected.")

doscarFile.close()

print("TOTAL GAPS:" +str(len(seriesList)))

gapList=[]
for series in seriesList:
    start=series[0][0]
    end=series[len(series)-1][0]
    gap=end-start
    gapList.append(gap) #In case, list is needed in the future. 
    print('Start:' +str(start)+' End:'+str(end)+' Gap:'+str(gap))

