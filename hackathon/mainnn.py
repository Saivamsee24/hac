# Import required libraries
import sys
import os
from tkinter import *
from PIL import ImageTk, Image
import subprocess

def function():
    win.destroy()
    subprocess.run([sys.executable, 'tk2.py'], check=True)
def function2():
    os.system("guide.pdf")

# Create an instance of tkinter window
win = Tk()
win.title("sign language translation")

# Define the geometry of the window
win.geometry("800x800")
win.wm_attributes('-transparentcolor','#ab23ff')
win.maxsize(800, 800)

frame = Frame(win, width=1772, height=1182)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("cd.jpeg"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()
label= Label(win, text= "SIGN LANGUAGE DETECTION", font=('DejaVu Sans Mono italic',38),bg='indianred1',fg='black')
label.pack(padx=30, pady=25,fill='x')

a = Button(text="LETS DIVE INTO TRANSLATION OF SIGNS! ",font=('DejaVu Sans Mono italic',15),height= 1, width= 38,command=function)
a.place(relx=0.5, rely=0.5, anchor=CENTER)
# a.pack(bg='white')
# a.config(bg="white", fg="black")
b = Button(text="Welcome to our project...(Guide)",font=('DejaVu Sans Mono italic',10),command=function2)
c = Button(text="Click here to exit the A5 Project...",font=('DejaVu Sans Mono italic',10),command = win.destroy)

b.place(x=20,y=200)
c.place(relx=0.93, rely=0.78, anchor=SE)

win.mainloop()