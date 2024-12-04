import tkinter as tk
from tkinter import messagebox

def check_triangle():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())
        
        if a <= 0 or b <= 0 or c <= 0:
            messagebox.showerror("Oshibka", "Dlinna storony treugol'nika dolzhna byt' polozhitel'nym chislom.")
            return
        
        if a == b == c:
            result = "Ravnostoronniy treugol'nik"
        elif a == b or b == c or a == c:
            result = "Ravnobedrenniy treugol'nik"
        else:
            result = "Raznostoronniy treugol'nik"
        
        messagebox.showinfo("Tip treugol'nika", result)
        
    except ValueError:
        messagebox.showerror("Oshibka", "Pozhaluysta, vvedite tselye chisla.")

# Sozdaem osnovnoe okno
root = tk.Tk()
root.title("Opredelenie tipa treugol'nika")

# Sozdaem polya vvod
label_a = tk.Label(root, text="Storona A:", bg="#F7F7F7", fg="#6B5B93", font=('Arial', 12))
label_a.pack()
entry_a = tk.Entry(root, font=('Arial', 12), fg="#333333", bg="#FFFFFF", insertbackground="#6B5B93")
entry_a.pack()

label_b = tk.Label(root, text="Storona B:", bg="#F7F7F7", fg="#6B5B93", font=('Arial', 12))
label_b.pack()
entry_b = tk.Entry(root, font=('Arial', 12), fg="#333333", bg="#FFFFFF", insertbackground="#6B5B93")
entry_b.pack()

label_c = tk.Label(root, text="Storona C:", bg="#F7F7F7", fg="#6B5B93", font=('Arial', 12))
label_c.pack()
entry_c = tk.Entry(root, font=('Arial', 12), fg="#333333", bg="#FFFFFF", insertbackground="#6B5B93")
entry_c.pack()

# Sozdaem knopku dlya proverki
check_button = tk.Button(root, text="Proverit'", command=check_triangle)
check_button.pack()

# Zapuskayem osnovnoy tsikl
root.mainloop()