#!/usr/bin/python3

import re


with open ('address.txt') as f:

    file=f.read()
    
    address= [["address" ]]        
    bloques= file.split('add ')
    for i in bloques:

        ipp= re.findall(r'(?<=address=)\w*[.]*\w*[.]*\w*[.]\w*\/*\w*', i)
        lista= re.findall(r'(?<=list=)\n*\w*[-]*\w*\n*',i)
        comment= re.findall(r'(?<=comment=)\n*\w*[.-]*\w*\n*|(?<=comment=\")\n*.*\n*(?=\")',i)
        
        if(len(comment) == 2):
            comment.pop(0)
        
        address.append(ipp+lista+comment) 
        
f.close()

with open('fortaddr.txt', 'w') as f1:
    
    f1.write('config firewall address' + '\n')
    for a in address:
        print(a)
        if len(a)< 2:
            continue
        else:
            
            ip=str(a[0])
            f1.write('edit ' + ip + '\n')
            if ip[0].isdigit():
                f1.write('set type ipmask' + '\n')       
                f1.write('set subnet '+ ip + '\n')

            else:
                f1.write('set type fqdn' + '\n')
                f1.write('set fqdn '+ ip + '\n')
            if len(a)==3:
                cm=str(a[2])
                f1.write('set comment ' + cm + '\n')
            f1.write('next'+ '\n')
            
    f1.write('end' + '\n')

    f1.write('config firewall addrgrp'  + '\n')
    for b in address:

        if len(b)< 2:
            continue
        else:
            ip=str(b[0])
            l=str(b[1]).strip()
            f1.write('edit '+ l +'\n')
            f1.write('config member '+ ip +'\n')
            f1.write('next'+ '\n')
    f1.write('end'+ '\n')

f1.close()