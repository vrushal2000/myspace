
from tkinter import *
root = Tk()
root.title("TEST YOUR KNOWLEDGE")
root.geometry("500x500")

title= "WELCOME TO THE ||TEST YOUR KNOWLEDGE|| LET'S SEE HOW YOU DO!"
my_label = Label(root, text= title, font=("Helvetica",10))
my_label.pack(pady=20)

q1="Signal Bandwidth is defined as the portion of _______ occupied by a signal.\na)Electromagnetic spectrum\nb)area\nc)waveform\nd)Channel:"
my_label = Label(root, text= q1, font=("Helvetica",10))
my_label.pack(pady=20)



def submit():
    
    my_label = Label(root, text= entry1 , font=("Helvetica",10))
    my_label.pack(pady=20)

entry1= Entry(root,width=20)
entry1.pack(pady=20)



my_button = Button(root, text='Submit', command= submit())
my_button.pack(pady=20)

 

root.mainloop()
