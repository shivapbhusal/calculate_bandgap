'''
A string equivalent series of BandGap
'''

myStr='abcdxxxmox' 

is_zero=False

resultList=[]
for letter in myStr:
    if letter!='x':
        before=letter
    if letter=='x':
        if len(resultList)==0:
            resultList.append(before)
        resultList.append(letter)
        is_zero=True

    if is_zero==True:
        if letter!='x':
            resultList.append(letter)
            break

print(resultList)
        
