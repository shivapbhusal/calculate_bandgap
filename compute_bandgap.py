'''
A python script to compute bandgap in zinc oxide
Requires 3 argument in command line: doscar file, series_begin and series_end 
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
result=[] # List to keep the result
is_zero=False

series_begin=stringToFloat(sys.argv[2])
series_end=stringToFloat(sys.argv[3])

'''
Reads each lines from the Doscar file, filtres out the lines with first column in the range -3 to 3. 
For each of these lines, finds the first occurance of 0 in the 2nd column
Appends the result until it finds the first occurance of non-zero. 
Appends the first first occurance of non-zero. 
The loop stops. 
'''
for lines in doscarFile:
    lines=lines.strip().split('  ')
    if stringToFloat(lines[0])>=series_begin and stringToFloat(lines[0])<=series_end: #Modify this line to customize the band size.
        if stringToFloat(lines[1])!=0:
            before = [stringToFloat(lines[0]),stringToFloat(lines[1])]
        if stringToFloat(lines[1])==0:
            if len(result)==0:
                result.append(before)
            result.append([stringToFloat(lines[0]),stringToFloat(lines[1])])
            is_zero=True
        if is_zero==True:
            print('Y is 0')
            if stringToFloat(lines[1])!=0:
                print('Stop here. This is the first occurance of non-zero')
                result.append([stringToFloat(lines[0]),stringToFloat(lines[1])])
                break
doscarFile.close()

print("Bandgap Series")
print(result) #Resulting Bandgap in the form of a list

start=result[1][0]
end=result[len(result)-1][0]

bandgap=end-start 

print('BandGap: ' +str(bandgap))
