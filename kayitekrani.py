import tkinter as tk
import mysql.connector

def show():
    yeniKayit()

def yeniKayit():
    def kayit():
        ad = entry_ad.get()
        soyad = entry_soyad.get()
        kullanici_adi = entry_kullanici_adi.get()
        sifre = entry_sifre.get()

        # Veritabanı bağlantısı
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Ataberk1*',
            database='kullanici_bilgileri'
        )

        cursor = db.cursor()

        # Kullanıcı kayıt sorgusu
        query = "INSERT INTO kullanici (ad, soyad, kullanici_adi, sifre) VALUES (%s, %s, %s, %s)"
        values = (ad, soyad, kullanici_adi, sifre)

        cursor.execute(query, values)
        db.commit()

        print(cursor.rowcount, "kayıt eklendi.")

        cursor.close()
        db.close()

    kayite = tk.Toplevel()
    kayite.title("BorsaBot")
    
    frame = tk.Frame(kayite)
    frame.pack()

    label_ad = tk.Label(frame, text="Adınız:")
    label_ad.pack()

    entry_ad = tk.Entry(frame)
    entry_ad.pack()

    label_soyad = tk.Label(frame, text="Soyisminiz:")
    label_soyad.pack()

    entry_soyad = tk.Entry(frame)
    entry_soyad.pack()

    label_kullanici_adi = tk.Label(frame, text="Kullanıcı Adınız:")
    label_kullanici_adi.pack()

    entry_kullanici_adi = tk.Entry(frame)
    entry_kullanici_adi.pack()

    label_sifre = tk.Label(frame, text="Şifreniz:")
    label_sifre.pack()

    entry_sifre = tk.Entry(frame, show="*")
    entry_sifre.pack()

    btn_kayit = tk.Button(frame, text="Kayıt Ol", command=kayit)
    btn_kayit.pack()

    kayite.mainloop()
