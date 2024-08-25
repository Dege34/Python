"""
Unutulanlar:
33
134
60
"""


import random
import time

class Kumanda():
    def __init__(self,tv_durum = "Kapalı",tv_ses = 0,tv_kanal_list = ["TrtÇOCUK","DegeTV","ShowTv"],tv_kanal_suan = "DegeTv"):
        self.tv_durum = tv_durum

        self.tv_ses = tv_ses

        self.tv_kanal_list = tv_kanal_list

        self.tv_kanal_suan = tv_kanal_suan

    def tv_ac(self):
        if (self.tv_durum == "Açık"):
            print("Zaten Açık")

        elif (self.tv_durum == "Kapalı"):
            print("TV açılıyor...")

    def tv_kapat(self):
        if (self.tv_durum == "Kapalı"):
            print("Zaten Kapalı")

        elif (self.tv_durum == "Açık"):
            print("TV Kapanıyor...")

    def ses_durum(self):

        while True:
            cevap = input("Sesi açmak için '>' Tuşlayın\nSesi Kapatmak için '<' Tuşlayın:\nÇıkış için 'çıkış' yaz\n")


            if (cevap == "<"):
                if (self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses Düzeyi:",self.tv_ses)

            if (cevap == ">"):
                if (self.tv_ses != 31):
                    self.tv_ses += 1
                    print("Ses Düzeyi:",self.tv_ses)

    def kanal_ekle(self,kanal):
        print("Kanal Eklendi",kanal)
        self.tv_kanal_list.append(kanal)


    def rasgele_kanal(self):

        rastgele = random.randint(0,len(self.tv_kanal_list)-1)

        self.tv_kanal_suan = self.tv_kanal_list[rastgele]

        print("Şu anki kanal:",self.tv_kanal_suan)

    def __len__(self):
        return "Kanal Sayısı:",len(self.tv_kanal_list)

    def __str__(self):
        return f"Tv Durum: {self.tv_durum}\nTvdeki  Şu anki Kanal: {self.tv_kanal_suan}"


kumanda = Kumanda()

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
    işlem = input("İşlem Girin:")

    işlem = int(işlem)
    if (işlem == "Q"):
        print("İşlem Menüsünden Çıkılıyor Bekleyin...")
        time.sleep(2)
        print("Güle Güle")

    elif işlem == 1:
        kumanda.tv_ac()

    elif işlem == 2:
        kumanda.tv_kapat()

    elif işlem == 3:
        kumanda.ses_durum()

    elif işlem == 4:
        kanal_ismi = input("Eklemek İstediğiniz Kanalları (,) ile ayırarak yazın")

        eklenecek = kanal_ismi.split(",")

        for i in eklenecek:
            kumanda.kanal_ekle(i)


    elif işlem == 5:
        print("Kanal Sayısı:",len(kumanda.tv_kanal_list))

    elif işlem == 6:
        kumanda.rasgele_kanal()

    elif işlem == 7:
        print(kumanda)

    else:
        print("Geçersiz İşlem")
























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































































