import pandas as pd
import matplotlib.pyplot as pl
import numpy as np

Phy= pd.read_csv('Phy.csv', header= None)
Phy= Phy[0]
Phy= list(Phy.values)

Chem= pd.read_csv('Chem.csv', header= None)
Chem= Chem[0]
Chem= list(Chem.values)

Math= pd.read_csv('Math.csv', header= None)
Math= Math[0]
Math= list(Math.values)

Eng= pd.read_csv('Eng.csv', header= None)
Eng= Eng[0]
Eng= list(Eng.values)

IP= pd.read_csv('IP.csv', header= None)
IP= IP[0]
IP= list(IP.values)

# print(Phy, Chem, Math, Eng, IP)

print('1) Phy')
print('2) Chem')
print('3) Math')
print('4) Eng')
print('5) IP')

sub= int(input('Subject?? '))

if sub== 1:
    nMark= int(input('Enter marks: '))
    Phy.append(nMark)
    Phy= pd.DataFrame({0: Phy})
    Phy.to_csv('Phy.csv', index= False, header=False)

elif sub==2:
    nMark= int(input('Enter marks: '))
    Chem.append(nMark)
    Chem= pd.DataFrame({0: Chem})
    Chem.to_csv('Chem.csv', index= False, header=False)
    
elif sub==3:
    nMark= int(input('Enter marks: '))
    Math.append(nMark)
    Math= pd.DataFrame({0: Math})
    Math.to_csv('Math.csv', index= False, header=False)

elif sub==4:
    nMark= int(input('Enter marks: '))
    Eng.append(nMark)
    Eng= pd.DataFrame({0: Eng})
    Eng.to_csv('Eng.csv', index= False, header=False)

elif sub==5:
    nMark= int(input('Enter marks: '))
    IP.append(nMark)
    IP= pd.DataFrame({0: IP})
    IP.to_csv('IP.csv', index= False, header=False)


Phy= pd.read_csv('Phy.csv', header= None)
Phy= Phy[0]
Phy= list(Phy.values)

Chem= pd.read_csv('Chem.csv', header= None)
Chem= Chem[0]
Chem= list(Chem.values)

Math= pd.read_csv('Math.csv', header= None)
Math= Math[0]
Math= list(Math.values)

Eng= pd.read_csv('Eng.csv', header= None)
Eng= Eng[0]
Eng= list(Eng.values)

IP= pd.read_csv('IP.csv', header= None)
IP= IP[0]
IP= list(IP.values)


pl.plot(range(len(Phy)), Phy, '#ff0000')
pl.plot(range(len(Chem)), Chem, '#ffa500')
pl.plot(range(len(Math)), Math, '#00ff00')
pl.plot(range(len(Eng)), Eng, '#00ffff')
pl.plot(range(len(IP)), IP, '#ff00ff')

pl.legend(['Phy', 'Chem', 'Math', 'Eng', 'IP'])

pl.savefig('Analysis.png')
pl.show()