# kwasy okienka

import math
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def calculate_ph():
    try:
        # Pobierz wartości wprowadzone przez użytkownika
        c = float(entry_concentration.get())
        K = float(entry_dissociation_constant.get())

        w = c / K
        if w >= 400:
            pH = -math.log10((K * K) ** (1 / 2))
        else:
            delta = K ** 2 + 4 * c * K
            alfa = (-K + math.sqrt(delta)) / (2 * c)
            pH = -math.log10(alfa * c)

        messagebox.showinfo("Wynik", f"Obliczone pH wynosi: {round(pH, 2)}")
    except ValueError:
        messagebox.showerror("Błąd", "Wprowadzone wartości muszą być liczbami")


# Utwórz główne okno
root = tk.Tk()
root.title("Kalkulator pH")

# Utwórz ramkę dla wprowadzonych danych
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

# Etykiety i pola tekstowe dla stężenia kwasu i stałej dysocjacji
tk.Label(frame_input, text="Stężenie kwasu:").grid(row=0, column=0, padx=5)
entry_concentration = tk.Entry(frame_input)
entry_concentration.grid(row=0, column=1, padx=5)
tk.Label(frame_input, text="Stała dysocjacji:").grid(row=1, column=0, padx=5)
entry_dissociation_constant = tk.Entry(frame_input)
entry_dissociation_constant.grid(row=1, column=1, padx=5)

# Przycisk do obliczania pH
btn_calculate = tk.Button(root, text="Oblicz pH", command=calculate_ph)
btn_calculate.pack(pady=5)

# Uruchom pętlę główną
root.mainloop()
