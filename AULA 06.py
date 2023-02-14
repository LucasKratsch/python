#LOGICA.PY
temp= float(input('Entre com a temperatura:'))
print(temp+1)


"""
Previsão do Tempo

quando a temperatura for menor que 0 = congelando
quando a temperatura for >=0 e <=20 = frio
quando a temperatura for >=21 e <=25 = normal
quando a temperatura for >=26 e <=35 quente
quando >35 Pelando de quente
"""

if temp <0:
    print('Congelando...')

elif 0 <= temp <= 20:
    print ('Frio...')
           
elif 21<= temp <=25:
    print('Normal...')
    
elif 26<= temp <=35:
    print ('Quente...')
    
else:
    print('Pelando de quente...')


