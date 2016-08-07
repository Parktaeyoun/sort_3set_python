'''
Created on 2016. 8. 8.

@author: enrjfenrjf
'''

import random

if __name__ == '__main__':
    
    f = open("randomNum.txt", "w")
    
    for i in range(5000):
        num = random.randrange(1,100000)
        f.write(str(num)+"\n")
        
    f.close
    
    
    
    