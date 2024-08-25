import random


class Hayvanlar():
    def __init__(self,renk = ["Pembe","Sarı","Siyah","Mavi","Mor","Yeşil","Turuncu","Beyaz","Cyan"],renk_suan = "Mavi",boy = ["Kısa","Uzun","Orta Boylu"],boy_suan = "Orta" ,yas = random.randint(0,50),yas_suan = 5,yetenek = ["Uçmak","Koşmak","Yürümek"]):
        self.renk = renk
        self.renk_suan = renk_suan
        self.boy = boy
        self.boy_suan = boy_suan
        self.yas = yas
        self.yas_suan = yas_suan
        self.yetenek = yetenek
    def rastgele_renk(self):
        rasgele = random.randint(0,len(self.renk)-1)
        renk_suan = self.renk[rasgele]
        return renk_suan

    def yasi(self):

        return self.yas

    def rastgele_boy(self):
        rasgele = random.randint(0,len(self.boy)-1)
        boy_suan = self.boy[rasgele]
        return boy_suan

    def __str__(self):
        return f"Hayvan Renk = {random.randint(0,len(self.renk)-1)}"

class Kuslar(Hayvanlar):


    def turleri(self,cins_ku = ["Martı","Kartal","Doğan","Şahin","Pağpağan","Muhabbet Kuşu"],cins_suan_ku = "Muhabbet Kuşu"):
        self.cins_ku = cins_ku
        self.cins_suan_ku = cins_suan_ku

        rasgele = random.randint(0, len(self.cins_ku) - 1)
        cins_suan_ku = self.cins_ku[rasgele]
        return cins_suan_ku

    def __str__(self):
        return f"Kuş Türü:{self.turleri()}\nKuş Yaşı:{self.yasi()}\nKuş Rengi:{self.rastgele_renk()}\nKuş Boyutu:{self.rastgele_boy()}"

class Kopekler(Hayvanlar):


    def turleri(self,cins_ko = ["Alman Köpeği","ChawChaw","Golden","Kurt","Süs Köpeği"],cins_suan_ko = "Süs Köpeği"):
        self.cins_ko = cins_ko
        self.cins_suan_ko = cins_suan_ko

        rasgele = random.randint(0, len(self.cins_ko) - 1)
        cins_suan_ko = self.cins_ko[rasgele]
        return cins_suan_ko

    def __str__(self):
        return f"Köpek Türü:{self.turleri()}\nKöpek Yaşı:{self.yasi()}\nKöpek Rengi:{self.rastgele_renk()}\nKöpek Boyutu:{self.rastgele_boy()}"

kopge = Kopekler()
kuss = Kuslar()
print(kuss)


