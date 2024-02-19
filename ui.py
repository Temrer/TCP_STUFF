import time
from tkinter import *


root = Tk()
root.geometry('1000x800')

chat_box = Text(root, height=30, width=80, pady=10, font=("Arial", 18, 'normal'))
chat_box.place(relx=.04, y=.0)

text_box = Entry(root, width=100)
text_box.place(relx=.03, rely=.95)
text_box.focus()

chat_box.insert(END, "Introduce your IP: \n")


def getIP(event=None):
    ip = text_box.get()
    with open("ServerAdress.txt", 'w') as file:
        file.write(f'IP=\"{ip}\"\n')
    text_box.delete(0, END)
    chat_box.insert(END, "Introduce your port: \n")
    root.bind('<Return>', getPort)


def getPort(event=None):
    chat_box.delete(1.0, END)
    port = text_box.get()
    with open("ServerAdress.txt", 'a') as file:
        file.write(f'PORT=\"{port}\"')
    chat_box.delete(1.0, END)
    text_box.delete(0, END)
    chat_box.insert(END, "IP added.")
    chat_box.after(2000, text_box.delete(1.0, END))


def messageSent(event):
    # chat_box.insert()
    pass


root.bind('<Return>', getIP)

root.mainloop()
