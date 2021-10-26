from tkinter import *
from tkinter.ttk import *

from time import strftime
root=Tk()
root.title("Time")

label=Label(root,font=('algerian',80),background="black",foreground="blue")
label.pack(anchor="center")
def getTime():
    t=strftime("%H : %M : %S : %p")
    label.config(text=t)
    label.after(1000,getTime)
getTime()
mainloop()