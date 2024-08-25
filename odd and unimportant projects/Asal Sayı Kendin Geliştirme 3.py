def asal_sayi(sayi):
    if (sayi == 0):
        return False
    if (sayi == 1):
        return False
    if (sayi == 2):
        return True
    else:
        for i in range(2,sayi):
            if (sayi % i == 0):
                return False

        return True

while True:
    sayi = input("Asal Sayı olduğunu Düşündüğün sayıyı yaz:")

    if (sayi == "q"):
        print("Programdan Çıkılıyor...")
        break

    else:
        sayi = int(sayi)

    if (asal_sayi(sayi)):
        print("Asal Sayıdır")

    else:
        print("Asal Sayı Değil")