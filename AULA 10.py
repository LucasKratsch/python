#matriz

#lista de número

numeros = [10,20,30,40,50,60,70,80,90]

soma= 0

for x in numeros:
    soma +=x
    
    print(numeros)

matriz =[
            [3,0],
            [2,-1],
            [5,7]
            ]
print(matriz)
print(matriz[0])
print(matriz[1])
print(matriz[2])

print('imprimindo com for')
for linha in matriz:
    for col in linha:
        print(col*2,end=' ')
    print()

import numpy as np

