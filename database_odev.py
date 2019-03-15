import sqlite3

con = sqlite3.connect("Python_Kurs.db")
cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Python_Kursu(AD TEXT, SOYAD TEXT,YAS INT, MAIL TEXT,CINSIYET TEXT, TELEFON INT)")
    con.commit()

def veri_ekle():
    ad = input("AD: ")
    soyad = input("SOYAD: ")
    yas = int(input("YAS: "))
    mail = input("MAIL: ")
    cinsiyet = input("CINSIYET: ")
    telefon = int(input("TELEFON: "))
    cursor.execute("INSERT INTO Python_Kursu VALUES(?,?,?,?,?,?)",(ad,soyad,yas,mail,cinsiyet,telefon))
    con.commit()

def verileri_goster():
    cursor.execute("SELECT * FROM Python_Kursu")
    liste = cursor.fetchall()
    for i in liste:
        print(i)

def verileri_sec(soyad):
    cursor.execute("SELECT * FROM Python_Kursu WHERE soyad = ?",(soyad,))
    liste2 = cursor.fetchall()
    for i in liste2:
        print(i)

def verileri_guncelle(eski_tel,yeni_tel):
    cursor.execute("UPDATE Python_Kursu SET TELEFON = ? WHERE TELEFON = ?",(yeni_tel, eski_tel))
    con.commit()

def verileri_sil(ad):
    cursor.execute("DELETE FROM Python_Kursu WHERE AD = ?",(ad,))
    con.commit()

tablo_olustur()

veri_ekle()
verileri_goster()