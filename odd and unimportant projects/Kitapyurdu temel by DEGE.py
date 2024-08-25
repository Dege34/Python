import sqlite3

import time

class Kitap():

    def __init__(self,isim,yazar,yayinevi,tür,baskı):
        self.isim = isim

        self.yazar = yazar

        self.yayinevi = yayinevi

        self.tür = tür

        self.baskı = baskı


    def __str__(self):

        return f"Kitap İsmi:{self.isim}\nKitap Yazarı: {self.yazar}\nKitap Yayınevi: {self.yayinevi}\nKitap Türü: {self.tür}\nKitap Baskı Sayısı: {self.baskı}"

class Kütüphane():

    def __init__(self):

        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("kütüphane.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists kitaplar (isim TEXT,yazar TEXT,yayinevi TEXT,tür TEXT,baskı INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()

    def baglanti_kes(self):

        self.baglanti.close()

    def kitapları_goster(self):

        sorgu = "Select * From kitaplar"

        self.cursor.execute(sorgu)

        kitaplar = self.cursor.fetchall()

        if (len (kitaplar) == 0):
            print("Kütüphanede Kitaplar NÂMEVCUT")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)

    def kitap_sorgula(self,isim):

        sorgu = "Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0):
            print("Kütüphanede Kitaplar NÂMEVCUT")

        else:

            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])

            print(kitap)

    def kitap_ekle(self,kitap):

        sorgu = "Insert into kitaplar Values(?,?,?,?,?)"

        self.cursor.execute(sorgu,(kitap.yazar,kitap.yazar,kitap.yayinevi,kitap.tür,kitap.baskı))

        self.baglanti.commit()

    def kitap_sil(self,isim):

        sorgu = "Delete From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        self.baglanti.commit()

    def baski_yukselt(self,isim):

        sorgu = "Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0):
            print("Kütüphanede Kitaplar NÂMEVCUT")

        else:
            baskı = kitaplar[0][4]

            baskı += 1

            sorgu2 = "Update kitaplar set baskı = ? where isim = ?"

            self.cursor.execute(sorgu2,(baskı,isim))

            self.baglanti.commit()


print("""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
Dege'nin Kütüphane Programına Hoşgeldiniz


Welcome to Dege's Library Program


Wilkommen zu Dege Bibliotek Programm 
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

İşlemler:

1)Kitapları Göster:

2)Kitap Sorgulama:

3)Kitap Ekle

4)Kitap Sil

5)Baskı Sayısı Güncelle

Çıkmak için "q" ya bas

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
""")


kütüphane = Kütüphane()

while True:

    işlem = input("Yapacağınız İşlem:")

    if (işlem == "q"):

        print("Kütüphaneden Çıkılıyor...")

        time.sleep(4)

        print("Bizi Tercih Ettiğiniz için Teşekkürler")

        break

    elif (işlem == "1"):
        kütüphane.kitapları_goster()

    elif (işlem == "2"):
        isim = input("Hangi Kitabı İstiyorsunuz ?:")

        print("Kitap Sorgulanıyor...")

        time.sleep(4)

        kütüphane.kitap_sorgula(isim)


    elif (işlem == "3"):
        isim = input("İsim:")

        yazar = input("Yazar:")

        yayinevi = input("Yayınevi:")

        tür = input("Tür:")

        baskı = int(input("Baskı:"))

        yeni_kitap = Kitap(isim,yazar,yayinevi,tür,baskı)

        print("Kitap Ekleniyor...")

        time.sleep(2)

        kütüphane.kitap_ekle(yeni_kitap)

        print("Kitap Eklendi.....")



    elif (işlem == "4"):
        isim = input("Hangi kitabı silmek istiyorsunuz ?")

        cevap = input("Emin Misiniz ? (E/H)")

        if (cevap == "E"):
            print("Kitap Siliniyor....")

            time.sleep(2)

            kütüphane.kitap_sil(isim)

            print("Kitap Silindi.")


    elif (işlem == "5"):
        isim = input("Hangi Kitabın baskısını yükseltmek istiyorsunuz ?:\n")

        print("Baskı Yükseltiliyor...")

        time.sleep(2)

        kütüphane.baski_yukselt(isim)

        print("Baskı Yükseltildi")


    else:
        print("Geçersiz İşlem.")