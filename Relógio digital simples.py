import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_time)

# Configuração da janela principal
root = tk.Tk()
root.title("Relógio Digital Simples")

# Configuração do rótulo para exibir o horário
label = tk.Label(root, font=('Arial', 48), background='black', foreground='white')
label.pack(anchor='center')

# Inicia a atualização do relógio
update_time()

# Inicia o loop principal da interface gráfica
root.mainloop()