"""
#---------------------------------------------------------------------------PASS ANAHTAR KELİMESİ
class yediyuzbir():
    def __init__ (self,isim,soyadi,oda_num,email,gelme_sirasi):
            self.isim = isim
            self.soyadi = soyadi
            self.oda_num = oda_num
            self.email = email
            self.gelme_sirasi = gelme_sirasi
    def bilgilerigoster(self):
        print(f"İsim: {self.isim}\nSoyadi: {self.soyadi}\nOda Numarası: {self.oda_num}\nE-mail: {self.email}\nOdaya {self.gelme_sirasi}. gelen kişi")
    def yeni_odaya_at(self,yeni_oda):
        self.oda_num = yeni_oda

    def oda_num_degis(self,room_num):
        self.gelme_sirasi = room_num

class yediyuzdort(yediyuzbir):
    pass
yaparak şimdilik class (yediyuzdort) = class (yediyuzbir)

"""


"""
#-----------------------------------------------------------------------Kendim Deneme
class yediyuzbir():
    def __init__ (self,isim,soyadi,oda_num,email,gelme_sirasi):
            self.isim = isim
            self.soyadi = soyadi
            self.oda_num = oda_num
            self.email = email
            self.gelme_sirasi = gelme_sirasi
    def bilgilerigoster(self):
        print(f"İsim: {self.isim}\nSoyadi: {self.soyadi}\nOda Numarası: {self.oda_num}\nE-mail: {self.email}\nOdaya {self.gelme_sirasi}. gelen kişi")
    def yeni_odaya_at(self,yeni_oda):
        self.oda_num = yeni_oda

    def oda_num_degis(self,room_num):
        self.gelme_sirasi = room_num

class yediyuzdort(yediyuzbir):
    def __init__ (self,isim,soyadi,oda_num,email,gelme_sirasi):
            self.isim = isim
            self.soyadi = soyadi
            self.oda_num = oda_num
            self.email = email
            self.gelme_sirasi = gelme_sirasi
    def bilgilerigoster(self):
        print(f"İsim: {self.isim}\nSoyadi: {self.soyadi}\nOda Numarası: {self.oda_num}\nE-mail: {self.email}\nOdaya {self.gelme_sirasi}. gelen kişi")

emre = yediyuzbir("Ali Emre","ARAR","701-4","emreyigotten@dege.com","3")
efe = yediyuzbir("Ali Efe","ERDİNÇ","701-2","efe@dege.com","2")
ege = yediyuzbir("Doğan Ege","BÜLTE","701-3","degebulte@dege.com","1")
batu = yediyuzbir("Kelami Batuhan","X","701-1","batucan@dege.com","4")
hasan = yediyuzdort("Hasan","X","704-2","hasanadana@dege.com","1")
ah_yavuz = yediyuzdort("AHHHHHHHHHHHHHHHHHHHHHHHHHH\n\t\tYAVUZ","X","704-1","ahyavuz@dege.com","2")
salak_emre = yediyuzdort("Salak ","Emre","704-3","salakemre@dege.com","3")

ah_yavuz.bilgilerigoster()
emre.yeni_odaya_at("704-4")
emre.oda_num_degis("4")
emre.bilgilerigoster()

"""
"""
-------------------------------------------------------------------------Super Anahtar Kelimesi
class Calisanlar():
    def __init__(self,isim,soyisim,numara,maas,eposta,departman):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maas = maas
        self.eposta = eposta
        self.departman = departman
    def bilgilerigoster(self):
        print(f"İsim: {self.isim}\nSoyisim: {self.soyisim}\nŞirket Numarası: {self.numara}\nMaaş: {self.maas}\nE-posta: {self.eposta}")




class Yoneticiler(Calisanlar):
    def __init__(self,isim,soyisim,numara,maas,eposta,departman):
        super().__init__(isim,soyisim,numara,maas,eposta,departman)

    def sirketten_at(self):

        print("İsim: X\nSoyisim: X\nŞirket Numarası: X\nMaaş: X\nE-posta: X")

    def maas_zam(self,ekle_maas):
        self.maas += ekle_maas

    def bilgilerigoster(self):
        print(f"İsim: {self.isim}\nSoyisim: {self.soyisim}\nŞirket Numarası: {self.numara}\nMaaş: {self.maas}\nE-posta: {self.eposta}")

yonetici = Yoneticiler("Ege","BÜLTE","1","30.000","degebulte@hotmail.com","CEO")

yonetici.sirketten_at()

"""
import time

class Kitaplar():
    def __init__(self,kitap_adi,yazar,yayinevi,kitap_turu,sayfa_sayisi):
        self.kitap_adi = kitap_adi
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.kitap_turu = kitap_turu
        self.sayfa_sayisi = sayfa_sayisi

    def __str__(self):
        return (f"Kitap Adı: {self.kitap_adi}\nYazar: {self.yazar}\nYayınevi: {self.yayinevi}\nKitap Türü: {self.kitap_turu}")

    def __len__(self):
        return self.sayfa_sayisi

    def __del__(self):
        print("Kitap Bilgileri Siliniyor...")
        time.sleep(1)
        print("Kitap Siteden Çıkarıldı.")

kitap_ilber = Kitaplar("Bir Ömür Nasıl Yaşanır","Prof.Dr.İlber Ortaylı","Dege Yayıncılık","Psikoloji",321)

print(kitap_ilber)














