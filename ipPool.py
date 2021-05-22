#!/usr/bin/python3

import re


with open ('ippool.txt') as f:

    file=f.read()
    
    ippools= [["ippool" ]]        
    bloques= file.split('add ')
    for i in bloques:
        name= re.findall(r'(?<=name=)\n*.*(?= ranges=)',i)
        rango1= re.findall(r'(?<=ranges=)\w*[.]*\w*[.]*\w*[.]\w*', i)
        rango2= re.findall(r'(?<=-)\w*[.]*\w*[.]*\w*[.]\w*',i)
        
        
        
        ippools.append(name+rango1+rango2) 
        
f.close()

with open('fortipool.txt', 'w') as f1:
    
    f1.write('config firewall ippool' + '\n')
    for a in ippools:
        print(a)
        if len(a)< 2:
            continue
        else:
            
            nombre=str(a[0])
            rang1=str(a[1])
            rang2=str(a[2])

            f1.write('edit ' + nombre + '\n')
            f1.write('set startip ' + rang1 + '\n')
            f1.write('set endip ' + rang2 + '\n')

            f1.write('next'+ '\n')
            
    f1.write('end' + '\n')

f1.close()