import tkinter as tk
import mysql.connector

def show():
    def login():
        username = entry_username.get()
        password = entry_password.get()

        # Veritabanı bağlantısı
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            #ADD PASSWORD HERE
            database='kullanici_bilgileri'
        )

        cursor = db.cursor()

        # Kullanıcı doğrulama sorgusu
        query = "SELECT * FROM kullanici WHERE kullanici_adi = %s AND sifre = %s"
        values = (username, password)
        cursor.execute(query, values)

        result = cursor.fetchone()

        if result:
            # Giriş başarılıysa yapılacak işlemler veya açılacak ekranlar
            label_username = tk.Label(giris_ekrani, text="Giriş başarılı")
            label_username.pack()
        else:
            label_username = tk.Label(giris_ekrani, text="Giriş Başarısız")
            label_username.pack()

        cursor.close()
        db.close()

    # Giriş ekranını oluştur
    giris_ekrani = tk.Toplevel()
    giris_ekrani.title("Giriş Yap")
    giris_ekrani.geometry("300x200")

    label_username = tk.Label(giris_ekrani, text="Kullanıcı Adı:")
    label_username.pack()

    entry_username = tk.Entry(giris_ekrani)
    entry_username.pack()

    label_password = tk.Label(giris_ekrani, text="Şifre:")
    label_password.pack()

    entry_password = tk.Entry(giris_ekrani, show="*")
    entry_password.pack()

    btn_login = tk.Button(giris_ekrani, text="Giriş Yap", command=login)
    btn_login.pack()

    

    giris_ekrani.mainloop()
