#!/usr/bin/python3

import re


with open ('datos.txt') as f:

    file=f.read()
    
    users= [["users" ]]        
    bloques= file.split('add')
    for i in bloques:
        #print('-------BLOQUE--------\n' + i + '\n')
        user= re.findall(r'(?<=name=)\n*.*\n*(?=password=)', i)     #el punto engloba todo excepto saltos de linea
        passw= re.findall(r'(?<=password=)\n*.*\n*(?=profile=)',i)
        
        users.append(user+passw)        
f.close()
with open('forti.txt', 'w') as f1:
    h=1
    f1.write('config firewall user' + '\n')
    for u in users:
        print(u)
        if len(u)!= 2:
            continue
        else:
            us=str(u[0])
            pw=str(u[1])
            f1.write('edit ' + str(h) + '\n')
            f1.write('set name ' + us.strip().strip('"').replace(' ', '')  + '\n')
            f1.write('set type password ' + pw.strip().replace(' ', '') + '\n')   #strip quita las \n \r \s de antes y despues del string
            f1.write('set status enable'+ '\n')
            f1.write('next'+ '\n')
            h= h+1
    f1.write('end')

f1.close()