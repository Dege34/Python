def not_hesaplama(satir):
    satir = satir[:-1]

    liste = satir.split(",")

    isim = liste[0]

    not1 = int(liste[1])

    not2 = int(liste[2])

    final = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + final * (4/10)

    if son_not >= 90:
        harf = "AA"

    elif son_not >= 85:
        harf = "AB"
    elif son_not >= 80:
        harf = "AB"
    elif son_not >= 75:
        harf = "BB"
    elif son_not >= 70:
        harf = "BC"
    elif son_not >= 65:
        harf = "CC"
    elif son_not >= 60:
        harf = "CD"
    elif son_not >= 55:
        harf = "DD"
    elif son_not >= 55:
        harf = "F"
    else:

        with open("C://Users/Doğan Ege BÜLTE/Desktop/Kalanlar.txt","a",encoding="utf-8") as file3:
            file3.write(isim)



with open("C://Users/Doğan Ege BÜLTE/Desktop/Notlar Python .txt","r",encoding = "utf-8") as file:
    eklenecek_liste = list()

    for i in file:
        eklenecek_liste.append(not_hesaplama(i))

    with open("C://Users/Doğan Ege BÜLTE/Desktop/5. Deneme.txt", "w", encoding="utf-8") as file2:
        for i in eklenecek_liste:
            file2.write(i)