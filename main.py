'''import tkinter as tk
import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
    user='root',
    password='ADD PASWORDHERE',
    db='deneme.db'
)

cursor = mydb.cursor()

def yeniKayit():
    ad = buton.get()
    soyad = buton2.get()

    sql = "INSERT INTO new_table (isim, soyisim) VALUES (%s, %s)"
    val = ad, soyad

    cursor.execute(sql, val)
    mydb.commit()

    print(cursor.rowcount, "kayıt eklendi.")



pencere = tk.Tk()
pencere.geometry("300x300+200+200")
pencere.title("Kripto Botu")

isim = tk.Label(text="Adınız")
isim.grid(row=0, column=0)

soyisim = tk.Label(text="Soyisminiz")
soyisim.grid(row=1, column=0)

buton = tk.Entry()
buton.grid(row=0, column=1)

buton2 = tk.Entry()
buton2.grid(row=1, column=1)

giris = tk.Button(text="Kaydet", command=yeniKayit, width=10)
giris.grid(row=2, column=1)





pencere.mainloop()

'''
