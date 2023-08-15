import tkinter as tk
import girisekrani
import kayitekrani

def open_giris_ekrani():
    girisekrani.show()

def open_kayit_ekrani():
    kayitekrani.show()

def exit_program():
    pencere1.destroy()

pencere1 = tk.Tk()
pencere1.title("BorsaBot")
pencere1.geometry("300x300")

hg = tk.Label(text="BorsaBot'a Hoşgeldiniz...")
hg.grid(row=0, column=1)

kayit = tk.Button(text="Giriş Yap!", command=open_giris_ekrani, width=10)
kayit.grid(row=2, column=2)

giris = tk.Button(text="Kayıt Ol!", command=open_kayit_ekrani, width=10)
giris.grid(row=2, column=1)

cikis = tk.Button(text="Çıkış", command=exit_program, width=10)
cikis.grid(row=3, column=1, columnspan=2)

pencere1.mainloop()