import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_time)

root = tk.Tk()
root.title("Relógio Digital Simples")

label = tk.Label(root, font=('Arial', 48), background='black', foreground='white')
label.pack(anchor='center')

update_time()

root.mainloop()
