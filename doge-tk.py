import tkinter as tk
from tkinter import messagebox as mb

def in1():
    mb.showinfo("doge", "the doge liked that :D")
def in2():
    mb.showinfo("doge", "the doge is mad D:")
def in3():
    mb.showerror("doge", "you killed the doge you monster")
    mb.showerror("doge", "how could you..")
    mb.showerror("doge", "don't come near me or my doges")
    exit("you killed the doge you monster how do you feel about yourself?")

tk.Button(text='pet doge', command=in1).pack(fill=tk.X)
tk.Button(text='feed doge', command=in1).pack(fill=tk.X)
tk.Button(text='good boy', command=in1).pack(fill=tk.X)
tk.Button(text='play with the doge', command=in1).pack(fill=tk.X)
tk.Button(text='take the ball form the doge', command=in2).pack(fill=tk.X)
tk.Button(text='give the doge the ball', command=in1).pack(fill=tk.X)
tk.Button(text='kill the doge..', command=in3).pack(fill=tk.X)
tk.mainloop()
