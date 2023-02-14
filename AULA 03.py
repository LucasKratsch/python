###CALCULADORA

import tkinter as tk
from tkinter import font, ttk

global erro

def vErro():
    global erro
    if erro:     #se erro igual true
        entrada.set('')
        erro = False

#funções Digita = D mais a tecla 

def v(c):
    if entrada.get()[-1] not in '+-/*,':
        d(c)

    elif entrada.get() and entrada.get()[-1] not in '+-/,':
        digita(c)






def d(c):
    entrada.set(entrada.get()+c)
    






def d0():#digita 0
    d('0')
    
def d1():#digita 1
     d('1')
    
def d2():#digita 2
     d('2')

def d3():#digita 3
    d('3')
    
def d4():#digita 4
     d('4')
    
def d5():#digita 5
     d('5')   

def d6():#digita 6
    d('6')
    
def d7():#digita 7
     d('7')
    
def d8():#digita 8
     d('8')

def d9():#digita 9
     d('9')

def dC():#digita clear (command + Shift C)
     entrada.set('') #set substitui, mas n existe nada para substituir
     vErro()

def dB():#digita o backspace e apaga (command + Shift B)
    texto = entrada.get()                  #posição: 01234
    entrada.set(texto[0:-1])#texto: '12+345
    vErro()
    
def dV():
    v(','),

                   


def dMa():
    v('+')
    


def dMe():
    v('-')
    
    

def dMULTI():
    v('*')
   
   

def dDIV():
    v('/')
     
   

def dIG():
    vErro()
    global erro #declara a variavel sem valor
    try:
        if entrada.get():
            r = entrada.get().replace(',','.')
            r = str(eval(r))
            r = r.replace('.',',')
            entrada.set(r)
           
        
    except Exception as e:
        entrada.set(e)
        erro = True         #atribui valor


def dE():
    dIGU

        
def okp(evento):
    c = evento.char

    if c == '.':
        c=','
        
    if c in '0123456789':
        entrada.set(entrada.get()+c)
        

    elif c == '-' and not entrada.get():    
        entrada.set ('-')


    elif c in ',+-/*' and entrada.get() and entrada.get() [-1] not in ',+-/*':
        entrada.set(entrada.get() + c)


    elif evento.keycode == 8 :
            entrada.set(entrada.get() [0:1])


    elif c in '=' and entrada.get():
                r=entrada.get().replace(',','.')


    
#eval faz calculo
#str mostra o resultado em string
            #troca porto por virgula
                r = r.replace('.',',')
                r = str(eval(r))
                
            
        
    
    
    
    
   




#cria objeto calculadora - é minha tela vazia
calc = tk.Tk()
calc.title("calc Tk 1.0")
calc.config(width=260, height=410)
calc.resizable(0,0)

entrada = tk.StringVar()



style = ttk.Style()
style.configure('Visor.TEntry',padding=5)


visor = ttk.Entry(calc,
                  style="Visor.TEntry",
                  width=19,
                  textvariable=entrada,
                  justify=tk.RIGHT,
                  font=font.Font(family="Arial",size=15),
                  state="disabled"
                  )
visor.place(x=10, y=10)
visor.focus()

#vincula um evento com uma função
visor.bind('<KeyPress>', okp)




#Backspace Clear +
btBack = tk.Button(calc, text='Backspace', height=2, width=14,command=dB).place(x=14, y=60)#cria o Botão, nome, tamanho e posição
btClear = tk.Button(calc, text='C', height=2, width=14, command=dC).place(x=130, y = 60)     #tk.Button, text,  altura, largura, x e y
btMais = tk.Button(calc, text='+', height=2, width=14, command=dMa).place(x=130, y = 110)
btMenos = tk.Button(calc, text='-', height=2, width=14, command=dMe).place(x=130, y = 160)
btDivisao = tk.Button(calc, text='/', height=2, width=14, command=dDIV).place(x=130, y = 210)
btMulti = tk.Button(calc, text='*', height=2, width=14, command=dMULTI).place(x=130, y = 260)
btIgual = tk.Button(calc, text='=', height=2, width=14, command=dIG).place(x=130, y = 310)
btMAISMemoria = tk.Button(calc, text='+M', height=2, width=6).place(x=130, y=360)
btMENOSMemoria = tk.Button(calc, text='-M', height=2, width=6).place(x=186, y=360)
btMemoria = tk.Button(calc, text='M', height=2, width=6).place(x=70, y=360)
btVirg = tk.Button(calc, text=',', height=2, width=6, command=dV).place(x=14, y=360)


bt1 = tk.Button(calc, text='1', height=2, width=6, command=d1).place(x=14, y=110)#O Command vincula a função(digita)ao botao
bt2 = tk.Button(calc, text='2', height=2, width=6, command=d2).place(x=70, y=110)  #vem após as coordenadas
bt3 = tk.Button(calc, text='3', height=2, width=6, command=d3).place(x=14, y=160)
bt4 = tk.Button(calc, text='4', height=2, width=6, command=d4).place(x=70, y=160)
bt5 = tk.Button(calc, text='5', height=2, width=6, command=d5).place(x=14, y=210)
bt6 = tk.Button(calc, text='6', height=2, width=6, command=d6).place(x=70, y=210)
bt7 = tk.Button(calc, text='7', height=2, width=6, command=d7).place(x=14, y=260)
bt8 = tk.Button(calc, text='8', height=2, width=6, command=d8).place(x=70, y=260)
bt9 = tk.Button(calc, text='9', height=2, width=6, command=d9).place(x=14, y=310)
bt0 = tk.Button(calc, text='0', height=2, width=6, command=d0).place(x=70, y=310)

calc.bind('<Return>',dE)
