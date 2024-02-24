import time
import tkinter as tk
from tkinter import ttk
from playsound import playsound

def start_countdown():
    my_time = int(time_entry.get())
    for x in range(my_time, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600) % 24
        countdown_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}", font=("Arial", int(root.winfo_width() / 15)))
        root.update()
        time.sleep(1)

    countdown_label.config(text="Süre Tamamlandı", font=("Arial", int(root.winfo_width() / 15)))
    # Süre bittiğinde ses çal
    playsound("")  # Ses dosyasının yolunu belirtmelisiniz


root = tk.Tk()
root.title("Geri Sayım Arayüzü")
root.configure(bg="black")  # Arka planı siyah yap
root.geometry("400x400") 


time_label = ttk.Label(root, text="Geri Sayım Süresi (saniye):", background="black", foreground="white")
time_label.pack(pady=10)

time_entry = ttk.Entry(root)
time_entry.pack(pady=5)

start_button = ttk.Button(root, text="Başlat", command=start_countdown)
start_button.pack(pady=5)

countdown_label = ttk.Label(root, text="", font=("Arial", int(root.winfo_width() / 15)), background="black", foreground="white")
countdown_label.pack(pady=10)

def on_resize(event):
    new_font_size = int(root.winfo_width() / 15)
    countdown_label.config(font=("Arial", new_font_size))
    time_label.config(font=("Arial", new_font_size-10))
    time_entry.config(font=("Arial", new_font_size-10))
    start_button.config(font=("Arial", new_font_size-20))
root.bind("<Configure>", on_resize)

root.mainloop()
