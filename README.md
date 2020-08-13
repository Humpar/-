# -
#tkinter库应用
#! python3
import tkinter as tk
room=tk.Tk()
room.title("hahaha")
room.resizable (500,500)
l=tk.Label(room,text='jab')
h=['s','d','gg','h','jk','l']
c='c'
for i in h:
    c+=i
    print(i)
    i=tk.Tk()
    i.title(c)
    
