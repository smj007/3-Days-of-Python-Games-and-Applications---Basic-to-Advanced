import tkinter
from tkinter import *


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def product(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

def LCM(a, b):
    L = a if a > b else b
    while L <= a*b:
        if L%a == 0 and L%b == 0:
            return L
        L = L - 1

def HCF(a, b):
    H = a if a < b else b
    while H >= 1:
        if a%H == 0 and b%H == 0:
            return H
        H = H - 1


def extract_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l


def calculate():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extract_from_text(text)
                r = operations[word.upper()](l[0], l[1])
                list.delete(0, END)
                list.insert(END, r)
            except:
                list.delete(0, END)
                list.insert(END, "Something went wrong here")
            finally:
                break

        elif word.upper() not in operations.keys():
            list.delete(0, END)
            list.insert(END, "Something went wrong here")




operations = {'ADD':add , 'ADDITION':add , 'SUM':add , 'PLUS':add ,
                'SUB':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
                 'LCM':LCM , 'HCF':HCF , 'PRODUCT':product , 'MULTIPLICATION':product,
                 'MULTIPLY':product , 'DIVISION':div , 'DIV':div ,'DIVIDE':div, 'MOD':mod ,
                  'REMANDER':mod , 'MODULUS':mod}


win = Tk()
win.geometry('500x300')
win.title("Smart Calculator")
win.configure(bg = 'lightskyblue')

l1 = Label(win, text = 'I am a smart calculator', width = 20, padx = 3)
l1.place(x = 150, y = 10)
l2 = Label(win, text = 'My name is sAI', padx = 3)
l2.place(x = 180, y = 40)
l3 = Label(win, text = 'What can I help you with?', padx = 3)
l3.place(x = 155, y = 130)

textin = StringVar()
e = Entry(win, width = 30, textvariable = textin)
e.place(x =140, y = 160)


button = Button(win, text = 'Just This', command = calculate)
button.place(x = 200, y = 200)

list = Listbox(win, width = 20, height = 3)
list.place(x = 170, y = 230)


win.mainloop()
