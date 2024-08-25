import time
import random
class Qumanda():
    def __init__(self,tv_durum = "Açık",tv_ses = 0,tv_kanal_list = ["Trt","DegeTv"],tv_kanalsuan = "DegeTv"):
        self.tv_durum = tv_durum

        self.tv_ses = tv_ses

        self.tv_kanal_list = tv_kanal_list

        self.tv_kanalsuan = tv_kanalsuan

    def tv_ac(self):
        if self.tv_durum == "Açık":
            print("Zaten Açık")
        else:
            print("Tv Açılıyor...")
            time.sleep(2)
            print("Hoş Geldin")
            self.tv_durum = "Açık"

    def tv_qapa(self):
        if self.tv_durum == "Kapalı":
            print("Zaten Kapalı")
        else:
            print("Tv Kapanıyor...")
            time.sleep(2)
            print("Güle Güle")
            self.tv_durum = "Kapalı"

    def ses_ac_kapa(self):
        while True:
            cevap = input("Sesi açmak için '>' Tuşlayın\nSesi Kapatmak için '<' Tuşlayın:\nÇıkış için 'çıkış' yaz\n")
            if self.tv_ses <= 0:
                print("Minimum ses karınca mısın aw")

            if (self.tv_ses != 0):
                if (self.tv_ses >= 31):
                    print("MAX SESSS DEDEEEEE")
                if (cevap == "<"):
                    self.tv_ses -= 1
                    print(f"Ses: {self.tv_ses}")
                elif (cevap == ">"):
                    self.tv_ses += 1
                    print(f"Ses: {self.tv_ses}")
                else:
                    print("Ses Güncellendi")
                    break
    def kanal_ekle(self,kanal):
        print("Kanal Eklendi",kanal)
        self.tv_kanal_list.append(kanal)

    def rasgele_kanal(self):
        rastgele = random.randint(0,len(tv_kanal_list)-1)

        self.tv_kanalsuan = self.tv_kanal_listtv_(rastgele)

    def __len__(self):
        return self.tv_kanal_list

    def __str__ (self):
        print(f"Tv Durum: {self.tv_durum}\nTv Ses Düzeyi: {self.tv_ses}\nTv Kanallar Listesi: {self.tv_kanal_list}\nTvdeki  Şu anki Kanal: {self.tv_kanalsuan}")

class Yedek_Tv(Qumanda):
    pass


kumanda = Qumanda()

print("""
*********************************************************

*
* *
*  *
*   *   ******* ********   *********
*    *  **      **         **
*     * ******* **         ********
*    *  **      **     *** **
*   *   **      **       * **
*  *    ******* ********** ********     TV ye hoş geldiniz
* *
*

1)TV AÇ

2)TV KAPA

3)SES DÜZEYİ

4)KANAL EKLE

5)KANAL SAYISI 

6)RANDOM KANAL

7)Tv Bilgileri Göster

Çıkmak için "Q" ya basın
**********************************************************
""")



while True:

    islem = input("İşlem Girin:")
    islem = int(islem)
    if str(islem) == "Q":
        print("Tv menüden çıkılıyor...")
        time.sleep(2)
        print("Çıkıldı.")
        break

    elif islem == 1:
        kumanda.tv_ac()

    elif islem == 2:
        kumanda.tv_qapa()

    elif islem == 3:
        kumanda.ses_ac_kapa()

    elif islem == 4:
        kanal_ismi = input("Eklemek İStediğin Kanalı  Girin (,) ekleyerek yazın:")

        tv_kanal_list = kanal_ismi.split(",")

        for eklenecekler in tv_kanal_list:
            kumanda.kanal_ismi(eklenecekler)

    elif islem == 5:
        print(len(tv_kanal_list))

    elif islem == 6:
        print("Kanal Sayısı:",len(Qumanda))

    elif islem == 7:
        print(Qumanda())

    else:
        print("Geçersiz İşlem")


