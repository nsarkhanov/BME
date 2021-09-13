import tkinter as tk 
import os

root=tk.Tk()
canvas=tk.Canvas(root,height=900,width=1200,bg='#212F3C')
canvas.pack()

frame=tk.Frame(root,background='#5F6A6A' )
frame.place(relheight=0.8,relwidth=0.8,relx=0.1,rely=0.1)

root.mainloop()