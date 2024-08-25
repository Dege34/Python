import datetime
import time
main_ag_ad = ["DegeWifi","EfeWifi","eMREGÖTTENWİFİ","KelamiWifi"]
main_ag_sifre = ["08062004","1","2","3"]
e = datetime.datetime.now()

class Bilgisayar():
    def __init__(self,pc_durum = "Açık",pc_ses = 0,mevcut_bluetooth = ["SONY WH-1000XMD","Apple İphone 13"],wifi = "Dege",):
        self.pc_durum = pc_durum
        self.pc_ses = pc_ses
        self.mevcut_bluetooth =mevcut_bluetooth
        self.wifi = wifi
    def pc_ac(self):
        if self.pc_durum == "Açık":
            print("Zaten Açık")
        else:
            print("Tv Açılıyor...")
            time.sleep(2)
            print("Hoş Geldin")
            self.pc_durum = "Açık"

    def pc_kapa(self):
        if self.pc_durum == "Kapalı":
            print("Zaten Kapalı")
        else:
            print("BIOS Kapanıyor...")
            time.sleep(2)
            print("Güle Güle")
            self.pc_durum = "Kapalı"

    def tarih_bugun(self):
        print("Güncel Tarih ve saat %s" % e)

    def ses_kontrol(self):
        while True:
            ses_cevap = input("Ses Açmak için (+)\nSes Kapatmak için (-)")

            if (self.pc_ses != 0):
                if (ses_cevap == "-"):
                    ses_cevap -= 1
                    print(f"{self.mevcut_bluetooth}\nSes Düzeyi: {self.pc_ses} ")
            if (self.pc_ses != 100):
                if (ses_cevap == "+"):
                    ses_cevap += 1
                    print(f"{self.mevcut_bluetooth}\nSes Düzeyi: {self.pc_ses} ")

    def bluetooth_ekle(self,cihaz_bluetooth):


        self.mevcut_bluetooth.append(cihaz_bluetooth)

        print("Cihaz Eklendi")

    def pc_pil(self,pc_pil_yuzde = 100):
        pc_pil = f"%{pc_pil_yuzde}"
        return pc_pil


    def wifi_ekle(self):
        eklenecek = input("Eklemek istediğn ağ adını gir:")
        time.sleep(2)
        eklenecek_sifre = input("Passport girin:")
        if eklenecek == main_ag_ad and eklenecek_sifre == main_ag_sifre:
            time.sleep(2)
            print("Ağa bağlandı")
        elif eklenecek != main_ag_ad:
            time.sleep(2)
            print("Wifi Ad bulunamadı Yanlış")

        elif eklenecek_sifre != main_ag_sifre:
            time.sleep(2)
            print("Wifi Şifre Yanlış")

        else:
            print("Bir sorun oldu Tekrar Deneyin")
    def __str__(self):
        return f"Pc Durum: {self.pc_durum}\nPc Ses {self.pc_ses}\nPc Bluetooth Kaynakları{self.mevcut_bluetooth}\nWifi Bağlantı {self.wifi}"

bilgisaayar =  Bilgisayar()

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
*  *    ******* ********** ********     BİOS a hoş geldiniz
* *
*

1)Pc AÇ

2)Pc KAPA

3)Ses DÜZEYİ

4)Bluetooth

5)Wifi

6)Tarih Göster

7) Bilgileri Göster

8)Pil Yüzdesi

BIOS'tan Çıkmak için "Q" ya basın
**********************************************************
""")


while True:

    islem = input("BIOS İşlem Girin:")

    islem = int(islem)

    if str(islem) == "Q":
        print("Tv menüden çıkılıyor...")
        time.sleep(2)
        print("Çıkıldı.")
        break

    elif islem == 1:
        bilgisaayar.pc_ac()

    elif islem == 2:
        bilgisaayar.pc_kapa()

    elif islem == 3:
        bilgisaayar.ses_kontrol()

    elif islem == 4:
        blue_tooth = input("Bluetooh ile Bağlanmak İstediğiniz Adı Girin:")


        bilgisaayar.bluetooth_ekle(blue_tooth)

        print(f"Mevcut Bluetooth Cihazları:{bilgisaayar.mevcut_bluetooth}")

    elif islem == 5:
        bilgisaayar.wifi_ekle()

    elif islem == 6:
        bilgisaayar.tarih_bugun()

    elif islem == 7:
        print(bilgisaayar)

    elif islem == 8:
        print(bilgisaayar.pc_pil())

    else:
        print("BIOS'TA BEKLENMEDİK HATA TEKRAR BAŞLATILIYOR...")
        time.sleep(2)
        break





