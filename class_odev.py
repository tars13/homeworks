
class Kurs():
    ogrenci_listesi = []

    def __init__(self,ad,soyad,yas,cinsiyet,mail,telefon):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.cinsiyet = cinsiyet
        self.mail = mail
        self.telefon = telefon
        self.ogrenci_listesi.append(self)

    def mevcudu_goruntuleme(self):
        for kişi in self.ogrenci_listesi:
            print(kişi.ad,kişi.soyad)

    def mevcut_sayisi(self):
        global mevcut
        mevcut = len(self.ogrenci_listesi)
        print("mevcut:{}".format(mevcut))


    def kurs_cinsiyet_orani(self):
        erkek = 0
        kadin = 0
        for i in self.ogrenci_listesi:
            if i.cinsiyet == "erkek":
                erkek += 1
            else:
                kadin += 1
        print("erkek orani : %",int(erkek*100/mevcut),"\nkadin orani : %",int(kadin*100/mevcut))

    def ogretmen_ihtiyaci(self):
        x = len(self.ogrenci_listesi) / 10
        if x < 1 :
            print("Ogretmen ihtiyaci: {}".format(1))
        else:
            print("Ogretmen ihtiyaci: {}".format(round(x)))

    def sinif_olustur(self):
        siniflar = []
        x = round(len(self.ogrenci_listesi) / 10)
        t = 0
        if x < 1:
            x = 1
        for i in range(x):
            siniflar.append([])
        for i in self.ogrenci_listesi:
            if len(siniflar[t]) <= 10:
                siniflar[t].append(i.ad)
            else:
                t += 1
        for i in range(x):
            print("{}. sinif : {}".format(i+1,siniflar[i]))




a1 = Kurs("irfan","python",24,"erkek","sdfsdv@gmail.com",654631232)
a2 = Kurs("maria","lima",22,"kadin","asdasf@gmail.com",321356156)
a3 = Kurs("taha","python",24,"erkek","sdfsdv@gmail.com",654631232)
a4 = Kurs("semih","python",24,"erkek","sdfsdv@gmail.com",654631232)
a5 = Kurs("furkan","python",24,"erkek","sdfsdv@gmail.com",654631232)
a6 = Kurs("arif","apython",24,"erkek","sdfsdv@gmail.com",654631232)
a7 = Kurs("neco","python",24,"erkek","sdfsdv@gmail.com",654631232)
a8 = Kurs("fatih","python",24,"erkek","sdfsdv@gmail.com",654631232)
a9 = Kurs("ahmet","pythonn",24,"erkek","sdfsdv@gmail.com",654631232)
a10 = Kurs("ali","python",24,"erkek","sdfsdv@gmail.com",654631232)
a11 = Kurs("bahadir","python",24,"erkek","sdfsdv@gmail.com",654631232)
a12 = Kurs("abdullah","python",24,"erkek","sdfsdv@gmail.com",654631232)
a13 = Kurs("cahit","python",24,"erkek","sdfsdv@gmail.com",654631232)
a14 = Kurs("yahya","python",24,"erkek","sdfsdv@gmail.com",654631232)
a15 = Kurs("murat","python",24,"erkek","sdfsdv@gmail.com",654631232)
a16 = Kurs("hzyf","python",24,"erkek","sdfsdv@gmail.com",654631232)


a1.mevcudu_goruntuleme()
a1.mevcut_sayisi()
a1.kurs_cinsiyet_orani()
a1.ogretmen_ihtiyaci()
a1.sinif_olustur()
