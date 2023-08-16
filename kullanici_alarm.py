'''import tkinter as tk
import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
    user='root',
    password=ADDPASWORDHERE,
    db='kullanici_bilgileri'
)
cursor = mydb.cursor()


def yeniKayit():
    ad = buton.get()
    soyad = buton2.get()
    kullanici_adi = buton3.get()
    sifre = buton4.get()

    sql = "INSERT INTO kullanici (ad,soyad,kullanici_adi,sifre) VALUES (%s, %s,%s,%s)"
    val = ad, soyad,kullanici_adi,sifre


    cursor.execute(sql, val)
    mydb.commit()

    print(cursor.rowcount, "kayıt eklendi.")



pencere = tk.Tk()

pencere.title("BorsaBot")

pencere.geometry("300x300+200+200")


isim = tk.Label(text="Adınız")
isim.grid(row=0, column=0)

soyisim = tk.Label(text="Soyisminiz")
soyisim.grid(row=1, column=0)

kullanici_adi = tk.Label(text="kullanıcı adınız")
kullanici_adi.grid(row=2, column=0)

sifre = tk.Label(text="şifreniz")
sifre.grid(row=3, column=0)

buton = tk.Entry()
buton.grid(row=0, column=1)

buton2 = tk.Entry()
buton2.grid(row=1, column=1)

buton3 = tk.Entry()
buton3.grid(row=2, column=1)

buton4 = tk.Entry()
buton4.grid(row=3, column=1)

giris = tk.Button(text="Kayıt Ol!", command=yeniKayit, width=10)
giris.grid(row=4, column=1)
pencere.mainloop()
'''
