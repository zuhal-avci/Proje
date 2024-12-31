import tkinter as tk


pencere = tk.Tk()
pencere.title("Arka Plan Rengi")
pencere.geometry("300x200")


def rengi_degistir():
    pencere.configure(bg="Red")


buton = tk.Button(pencere, text="Rengi Değiştir", command=rengi_degistir)
buton.pack(pady=20)


pencere.mainloop()
