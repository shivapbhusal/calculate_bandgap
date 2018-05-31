'''
A string equivalent series of BandGap
'''

myStr='abcdxxxmox' 

is_zero=False

for letter in myStr:
    if letter=='x':
        print(letter)
        is_zero=True

    if is_zero==True:
        if letter!='x':
            print(letter)
            break
        
