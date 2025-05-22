import tkinter as tk
from datetime import datetime
import pytz
import requests

def get_planet_alignment():
    try:
        response = requests.get("https://starwalk.space/pt/news/what-is-planet-parade")
        if response.status_code == 200:
            data = response.json()
            return data.get("alignment", "Informação indisponível")
        else:
            return "Erro ao obter alinhamento"
    except Exception as e:
        return f"Erro: {e}"

def update_clock():
    now_utc = datetime.now(pytz.utc)
    now_ny = now_utc.astimezone(pytz.timezone("America/New_York"))
    now_london = now_utc.astimezone(pytz.timezone("Europe/London"))
    now_tokyo = now_utc.astimezone(pytz.timezone("Asia/Tokyo"))

    utc_time.set(f"UTC: {now_utc.strftime('%Y-%m-%d %H:%M:%S')}")
    ny_time.set(f"Nova York: {now_ny.strftime('%Y-%m-%d %H:%M:%S')}")
    london_time.set(f"Londres: {now_london.strftime('%Y-%m-%d %H:%M:%S')}")
    tokyo_time.set(f"Tóquio: {now_tokyo.strftime('%Y-%m-%d %H:%M:%S')}")

    root.after(1000, update_clock)

root = tk.Tk()
root.title("Relógio Digital Complexo")

utc_time = tk.StringVar()
ny_time = tk.StringVar()
london_time = tk.StringVar()
tokyo_time = tk.StringVar()

tk.Label(root, textvariable=utc_time, font=("Helvetica", 14)).pack()
tk.Label(root, textvariable=ny_time, font=("Helvetica", 14)).pack()
tk.Label(root, textvariable=london_time, font=("Helvetica", 14)).pack()
tk.Label(root, textvariable=tokyo_time, font=("Helvetica", 14)).pack()

alignment = get_planet_alignment()
tk.Label(root, text=f"Alinhamento dos planetas: {alignment}", font=("Helvetica", 12), fg="blue").pack()

update_clock()
root.mainloop()
# Obs: A parte do alinhamento dos planetas ainda não funciona direito.
# O site que usei não tem uma API própria, então preciso pesquisar uma forma melhor
# de puxar esses dados e ligar isso ao relógio.
