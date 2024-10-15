
import tkinter as tk
from tkinter import ttk

def ent(valor):
    var = float(entry2.index(tk.INSERT))
    var = str(int(var))
    print(var)
    entry2.insert(tk.END, var+' '+valor+ '\n')

root = tk.Tk()
root.config(width=400, height=300)
# Create the textbox.
entry = ttk.Entry()

entry.insert(0, "Hello world!")
# entry.insert(0, "Hello")
# entry.insert(5, " world!")
entry.insert(0, "Hello")

entry.insert(tk.END, " world!")

#entry = ttk.Entry(state=tk.DISABLED)
#entry = ttk.Entry(state="readonly")
entry.place(x=50, y=50)
button = ttk.Button(text="Get text", command=lambda: print(entry.get()))
button.place(x=50, y=100)
#button2 = ttk.Button(text="Get text2", command=lambda: ent("textou"))
button2 = ttk.Button(text="Get text2", command=lambda: ent(entry.get()))
button2.place(x=150, y=100)
# Place it within the window.

entry2 = tk.Text(width=30, height=5) #ttk.Entry(takefocus=False)
entry2.place(x=70, y=150)
entry2.insert(tk.END, " world1!")
print(entry2.index(tk.INSERT))
entry2.insert(tk.END, " world2!")
print(entry2.index(tk.INSERT))
entry2.insert(tk.END, " world3!"+'\n')
print(entry2.index(tk.INSERT))
var = float(entry2.index(tk.INSERT))+1.0
print(var)
var = 2.0
entry2.insert(var, " world4!"+'\n')
print(entry2.index(tk.INSERT))
root.mainloop()