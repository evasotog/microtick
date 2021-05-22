#!/usr/bin/python3

import re


with open ('routes.txt') as f, open('fortiroute.txt', 'w') as f1:

    file=f.read()
    
    f1.write('config router static' + '\n')
    h=0
    bloques= file.split('add ')
    for i in bloques:
        if(h==0):
            h=1
            continue
        f1.write('edit ' + str(h) + '\n')
        gatw= re.findall(r'(?<=gateway=)\n*\w*[.]*\w*[.]*\w*[.]\w*\/*\w*', i)
        if len(gatw)>0:
            f1.write('set gateway ' + gatw[0].strip() + '\n')
        dest= re.findall(r'(?<=dst-address=)\n*\w*[.]*\w*[.]*\w*[.]\w*\/*\w*', i)
        if len(dest)>0:
            f1.write('set dst ' + dest[0].strip() + '\n')
        distance= re.findall(r'(?<=distance=)\n*\w',i)
        if len(distance)>0:
            f1.write('set priority '+ distance[0].strip() + '\n')
        dis= re.findall(r'(?<=disabled=)\n*\w',i)
        if len(dis)>0 and dis[0].strip()== "y":
            f1.write('set status disable' +'\n')
        comment= re.findall(r'(?<=comment=\")\n*.*\n*(?=\")|(?<=comment=)\n*\w*[.-]*\w*\n*',i)
        if(len(comment) == 2):
            comment.pop(0)  #creo que se puede quitar
        if len(comment)>0:
            f1.write('set comment ' + comment[0].strip("\n") + '\n')
        f1.write('next'+ '\n')
        h = h+1
    f1.write('end' + '\n')
    
       
f1.close()
f.close()
