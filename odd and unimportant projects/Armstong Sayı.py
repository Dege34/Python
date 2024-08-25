def armstong(sayi):
    armstong_list =list()
    for i in sayi:
        armstong_list.append(sum(i**len(sayi)))
        if armstong_list ==sayi:
            return True
        else:
            return False



while True:
    sayi = input("Armstong Olduğunu Düşündüğünüz Sayıyı Yazın:")

    if (sayi =="q"):
        print("Program Sonlanıyor...")
        break
    else:
        sayi = int(sayi)
        if (armstong(sayi)==True):
            print("Armstong Sayı")
        else:
            print("Armstong Sayı Değil")

