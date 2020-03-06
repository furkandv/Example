# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 20:14:58 2020

@author: FurkanDvv

Program kaç saniyede çalışıyor.
"""

import time

def main():
    for i in range(1000):
        print(i)
        
        
if __name__ == "__main__":
    
    startTime = time.time()
    main()
    endTime = time.time()
    
    totalTime = endTime - startTime
    print(' Time: ' , totalTime)