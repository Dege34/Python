"""
class cikolata():
    def __init__(self,üretim_tarihi,Marka,renk):
        self.üretim_tarihi = üretim_tarihi
        self.Marka = Marka
        self.renk = renk

nesle = cikolata(1990,"Nesle","beyaz")

ulker = cikolata(2000,"Ülker","Bitter")

tobleron = cikolata(1880,"Tobleron","Sütlü")

print(tobleron.renk)

print(ulker.renk)

print(nesle.üretim_tarihi)

class yediyüzbirinci_koguş():
    def __init__(self,ad,yas,kilo,cmmmmmmmmmmmm):
        self.ad = ad
        self.yas = yas
        self.kilo = kilo
        self.cmmmmmmmmmmmm = cmmmmmmmmmmmm

birDE_kogus = yediyüzbirinci_koguş("dEGE",18,50,100)
ikiEF_kogus = yediyüzbirinci_koguş("HaliEfe",18,50,99)
üçEM_kogus = yediyüzbirinci_koguş("Emre",77,62,1)
dortKE_kogus = yediyüzbirinci_koguş("Kelami",18,51,98)

print(birDE_kogus.ad)
print(üçEM_kogus.cmmmmmmmmmmmm)
"""
"""
class yediyuzbir():
    def __init__(self,isim,soyisim,numara,maas,yil,mail,dil):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maas = maas
        self.yil = yil
        self.mail = mail
        self.dil = dil
    def bilgilerigoster(self):
        print("""
        İsim: {}
        
        Soyisim: {}        
        
        Numara: {}
        
        Maaş: {}
        
        {} Yıldır Bizimle
        
        Maili: {}
        
        Bildiği Kodlama Dilleri: {}
        """.format(self.isim,self.soyisim,self.numara,self.maas,self.yil,self.mail,self.dil))

    def zammaas(self,maasmiktarı):
        print("Bilgiler İşleniyor Bebiş")
        self.maas += maasmiktarı


    def yenidil(self,ekledil):
        print("Dil Ekleniyoreeee")
        self.dil.append(ekledil)


emre = yediyuzbir("Ali Emre","ARAR",31,10.000,2,"emremanyakverici@hotmail.com","egeyi götten sikmek")

ege = yediyuzbir("KİNG DEGE","ARAR",311,100.000,30,"degebulte@hotmail.com","Python,C+,Java,Assembly,Go")

efe = yediyuzbir("Ali Efe","ERDİNÇ",3111,11.000,3,"efepython@hotmail.com","Pythonu Türkçeden Daha İyi Biliyor")

kelami = yediyuzbir("Kelami Batuhan","BÖLÜKBAŞI",31111,10.000,2.5,"kelamianimeci@hotmail.com","Junior Python")

print(emre.bilgilerigoster())

"""














