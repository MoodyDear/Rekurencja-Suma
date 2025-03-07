import tkinter as tk
from tkinter import messagebox

def rekurencyjna_suma(n):
    if n == 0:
        return 0
    return n + rekurencyjna_suma(n - 1)

def oblicz_sume():
    try:
        n = int(entry.get())
        if n < 0:
            messagebox.showerror("Błąd", "Podaj liczbę większą lub równą 0")
            return
        wynik = rekurencyjna_suma(n)
        messagebox.showinfo("Wynik", f"Suma liczb od 1 do {n}: {wynik}")
    except ValueError:
        messagebox.showerror("Błąd", "Podaj poprawną liczbę całkowitą")

root = tk.Tk()
root.title("Rekurencyjne Sumowanie")
root.geometry("300x200")

tk.Label(root, text="Podaj liczbę:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Oblicz sumę", command=oblicz_sume).pack(pady=20)

root.mainloop()