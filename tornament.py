
import re
from decimal import Decimal
user_input = input("enter number: \n")
selnum = []
leng = 0



def tornament():
    Values = re.findall('\-?\d+', user_input)
    for elem in Values:
        selnum.append(int(elem))
        leng = len(selnum)
    while leng > 1:
        
        if selnum[0] < selnum[1]:
            selnum.remove(selnum[1])
            
        else:
            selnum.remove(selnum[0])
            
        
        leng = leng - 1
    return selnum
        

print(tornament())
