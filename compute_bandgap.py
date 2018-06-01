'''
A python script to compute bandgap in zinc oxide
'''

import sys

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
result=[]
is_zero=False
for lines in doscarFile:
    lines=lines.strip().split('  ')
    if stringToFloat(lines[0])>=-3 and stringToFloat(lines[0])<=3:
        if stringToFloat(lines[1])==0:
            result.append([stringToFloat(lines[0]),stringToFloat(lines[1])])
            is_zero=True
        if is_zero==True:
            print('Y values are 0')
            if stringToFloat(lines[1])!=0:
                print('Stop here. This is the first occurance of non-zero')
                result.append([stringToFloat(lines[0]),stringToFloat(lines[1])])
                break
doscarFile.close()

print("Bandgap Series")
print(result) #Resulting Bandgap in the form of a list

start=result[0][0]
end=result[len(result)-1][0]

bandgap=end-start

print('BandGap: ' +str(bandgap))
