import tkinter as tk
from tkinter import filedialog, Text
import os
import tkinter
import tkinter.scrolledtext

root = tk.Tk()

canvas = tk.Canvas(root, height= 400, width=600, bg="#1A6BBC")
canvas.pack()

frame = tkinter.scrolledtext.ScrolledText(root, bg="#1C2833")
frame.place(relwidth=0.8, relheight=0.4, relx=0.1, rely=0.1)
frame.config(state='disabled')

buttonFrame = tk.Frame(bg="#1C2833")
buttonFrame.place(relwidth=0.5, relheight=0.1, relx=0.252, rely=0.7)

runProgram = tk.Button(canvas, text="Talk to U.N.I.T", padx=10, pady = 5, fg = "#33C518", bg = "#1C2833")
runProgram.pack()


root.mainloop()