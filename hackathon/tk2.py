from tkinter import *
import sys
import os
import subprocess

root=Tk()
root.geometry("695x240")
root.maxsize(695,240)
root.minsize(695,240)


def hello1():
    # os.system('level1.py')
    subprocess.run([sys.executable, 'level1.py'], check=True)

def hello2():
    subprocess.run([sys.executable, 'level2.py'], check=True)


def hello3():
    subprocess.run([sys.executable, 'main.py'], check=True)

frame=Frame(root,borderwidth=100,bg='grey',relief=SUNKEN)
frame.pack(side=LEFT,anchor='nw')

b1=Button(frame,fg='black',text="NUMBERS",font='bold',command=hello1)
b1.pack(side=LEFT,padx=23,fill='x')

b2=Button(frame,fg='black',text="SYMBOLS",font='bold',command=hello2)
b2.pack(side=LEFT,padx=23,fill='x')

b3=Button(frame,fg='black',text="FUNCTIONS",font='bold',command=hello3)
b3.pack(side=RIGHT,padx=23,fill='x')




root.mainloop()