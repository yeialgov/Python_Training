# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:08:06 2019

@author: Yeisson Alirio
"""


def dup_1(Lista):
    Lista.sort()
    Lista_new=[]
    for i in Lista:
        if Lista.count(i)==1:
            Lista_new.append(i)
        else:
          if i not in Lista_new:
             Lista_new.append(i)      
    print(Lista_new)

def dup_2(Lista):
    Lista=set(Lista)
    Lista=list(Lista)
    print(Lista)

import random
a=[]
for i in range(0,10):
    a.append(random.randint(0,6))
print(a)

b=[5, 4, 5, 1, 2, 5, 4, 4, 3, 5]

dup_1(a)  
dup_2(a)
