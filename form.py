import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image
import numpy as np

window= tk.Tk()
window.title("face recognition system")

l1= tk.Label(window,text= 'name',font=('Algerian',20))
l1.grid(column=0,row=0)
t1=tk.Entry(window,width=50,bd=5)
t1.grid(column= 1 , row= 0)

l2= tk.Label(window,text= 'age',font=('Algerian',20))
l2.grid(column=0,row=1)
t2=tk.Entry(window,width=50,bd=5)
t2.grid(column= 1 , row= 1)

l3= tk.Label(window,text= 'address',font=('Algerian',20))
l3.grid(column=0,row=2)
t3=tk.Entry(window,width=50,bd=5)
t3.grid(column= 1 , row= 2)

b1= tk.Button(window,text= 'trainning',font=('Alderian',20),bg='orange',fg='red')
b1.grid(column=0,row=4)

b2= tk.Button(window,text= 'detect the face',font=('Alderian',20),bg='orange',fg='red')
b2.grid(column=1,row=4)

#def generate_dataset():


b3= tk.Button(window,text= 'generate dataset',font=('Alderian',20),bg='orange',fg='red',)
b3.grid(column=2,row=4)

window.geometry("800x200")
window.mainloop()



