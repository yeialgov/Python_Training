# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 16:24:41 2019

@author: Yeisson Alirio
"""
import random    
Passwort=[]
sug = ['Katze', 'Hunde', 'Pferd']
A = 'ASDFGHJKLPOIUZTREWQ'
a = 'eurjkjljhgrtiuendwo'
pass_str = input('How strong would you like your password?: ')
if pass_str=='strong':
    n = 10
    Passwort=[random.randint(1,6) for i in range (random.randint(2,4))]
    Passwort.append(random.choice(A))
    Passwort.append(random.choice(a))
    Passwort.append(random.choice(A))
    End = [random.randint(5,9)for i in range (random.randint(3,5))]
    Passwort.extend(End)
else:
    n = 2
    Passwort.append(random.choice(sug))
    End = [random.randint(1,6) for i in range (n)]
    Passwort.extend(End)
    
Passwort = [str(Passwort[i]) for i in range (len(Passwort))]
separator = ''
Passwort = separator.join(Passwort)
print ('Suggested Passwort: '+Passwort)
