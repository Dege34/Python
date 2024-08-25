"""
def not_okuma(satir):

    print(satir)


with open("C:/Users/Doğan Ege BÜLTE/Desktop/Notlar Python .txt","r",encoding = "utf-8") as file:

    for i in file:
        not_okuma(i)

Output():
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Doğan Ege BÜLTE,100,100,100

Ali Emre ARAR,1,2,3

Kelami Batuhan BÖLÜKBAŞI,100,90,100

Ali Efe ERDİNÇ,100,89,100

Hatice Günday,70,90,20

Mustafa Akyürek,90,80,60

Ramazan Topaloğlu,60,30,50

Elif Akşit,80,40,80

Mehmet Düşenkalkar,70,20,40

Hatice Dağdaş,90,90,80

Merve Tütüncü,40,30,30

Hatice Pekkan,50,70,60

Merve Alyanak,70,60,30

Meryem Aşıkoğlu,20,80,70

Süleyman Uluhan,40,10,100

Esra Ekici,10,10,30

Emine Kumcuoğlu,90,30,80

Süleyman Kumcuoğlu,50,10,60

Şerife Kumcuoğlu,40,70,70

Sude Tekand,90,50,90

Elif Nebioğlu,10,10,60

Sude Berberoğlu,10,100,50

Yasemin Durmaz,40,70,10

Fadime Akyürek,50,20,100

Fatma Akşit,60,40,90

Emre Sözeri,50,50,20

Yasemin Kurutluoğlu,40,50,40

Fatma Akman,80,20,30

Hacer Korol,80,50,90

Recep Altınbaş,40,70,80

Murat Numanoğlu,70,100,100

Fatih Fahri,40,10,10

Halil Sarıoğlu,30,70,60

Merve Arıcan,30,30,70

İsmail Kaplangı,60,50,10

Emir Egeli,80,20,80

Havva Erbulak,30,10,80

Hacer Okumuş,70,100,70

Salih Ağaoğlu,10,10,40

Zeliha Ağaoğlu,100,80,30

Abdullah Solmaz,60,40,50

Fatih Elmastaşoğlu,20,20,60

Hacer Karaer,90,90,60

Sude Kumcuoğlu,60,20,30

Abdullah Kuzucu,100,40,40

Hanife Söyler,100,20,80

Sude Orbay,60,30,40

Sultan Uluç,90,90,30

Hanife Beşok,80,100,50

Hülya Karadaş,80,100,10

Fatma Tuğluk,60,20,50

Halil Güçlü,100,80,30

Recep Eronat,60,100,20

Büşra Koyuncu,60,70,70

Hüseyin Kunt,50,80,10

Halil Numanoğlu,70,60,40

Hülya Gürmen,80,100,30

Ömer Kulaksızoğlu,40,40,60

Zeliha Demirel,70,40,100

Mustafa Aşıkoğlu,60,70,90

Süleyman Orbay,90,80,60

İbrahim Erez,50,60,40

Süleyman Koçyiğit,100,10,60

Salih Orbay,60,10,30

Şerife Süleymanoğlu,80,30,100

Murat Adal,10,90,100

Osman Aybar,50,20,100

Sude Balcı,60,10,40

Zeynep Koyuncu,50,90,50

İbrahim Pekkan,20,10,60

Fatih Erdoğan,30,60,30

Abdullah Ekşioğlu,40,60,10

Osman Adan,30,90,50

Ramazan Paksüt,90,20,20

Halil Gökgöz,80,10,20

Emre Kurutluoğlu,70,80,100

Mahmut Akışık,40,80,20

Yusuf Hamzaoğlu,100,40,90

Ali Akan,90,90,80

Zeliha Beşerler,100,80,20

Ali Oraloğlu,20,20,90

Hanife Poçan,100,50,10

Ayşe Kurutluoğlu,50,10,80

Fatih Akman,100,10,60

Mehmet Babacan,70,60,60
---------
Bizim her satır sonunda \n imiz var bundan kurtulmak için

def not_okuma(satir):

    satir = satir[:-1]

    print(satir)


with open("C:/Users/Doğan Ege BÜLTE/Desktop/Notlar Python .txt","r",encoding = "utf-8") as file:

    for i in file:
        not_okuma(i)

Output():
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Doğan Ege BÜLTE,100,100,100
Ali Emre ARAR,1,2,3
Kelami Batuhan BÖLÜKBAŞI,100,90,100
Ali Efe ERDİNÇ,100,89,100
Hatice Günday,70,90,20
Mustafa Akyürek,90,80,60
Ramazan Topaloğlu,60,30,50
Elif Akşit,80,40,80
Mehmet Düşenkalkar,70,20,40
Hatice Dağdaş,90,90,80
Merve Tütüncü,40,30,30
Hatice Pekkan,50,70,60
Merve Alyanak,70,60,30
Meryem Aşıkoğlu,20,80,70
Süleyman Uluhan,40,10,100
Esra Ekici,10,10,30
Emine Kumcuoğlu,90,30,80
Süleyman Kumcuoğlu,50,10,60
Şerife Kumcuoğlu,40,70,70
Sude Tekand,90,50,90
Elif Nebioğlu,10,10,60
Sude Berberoğlu,10,100,50
Yasemin Durmaz,40,70,10
Fadime Akyürek,50,20,100
Fatma Akşit,60,40,90
Emre Sözeri,50,50,20
Yasemin Kurutluoğlu,40,50,40
Fatma Akman,80,20,30
Hacer Korol,80,50,90
Recep Altınbaş,40,70,80
Murat Numanoğlu,70,100,100
Fatih Fahri,40,10,10
Halil Sarıoğlu,30,70,60
Merve Arıcan,30,30,70
İsmail Kaplangı,60,50,10
Emir Egeli,80,20,80
Havva Erbulak,30,10,80
Hacer Okumuş,70,100,70
Salih Ağaoğlu,10,10,40
Zeliha Ağaoğlu,100,80,30
Abdullah Solmaz,60,40,50
Fatih Elmastaşoğlu,20,20,60
Hacer Karaer,90,90,60
Sude Kumcuoğlu,60,20,30
Abdullah Kuzucu,100,40,40
Hanife Söyler,100,20,80
Sude Orbay,60,30,40
Sultan Uluç,90,90,30
Hanife Beşok,80,100,50
Hülya Karadaş,80,100,10
Fatma Tuğluk,60,20,50
Halil Güçlü,100,80,30
Recep Eronat,60,100,20
Büşra Koyuncu,60,70,70
Hüseyin Kunt,50,80,10
Halil Numanoğlu,70,60,40
Hülya Gürmen,80,100,30
Ömer Kulaksızoğlu,40,40,60
Zeliha Demirel,70,40,100
Mustafa Aşıkoğlu,60,70,90
Süleyman Orbay,90,80,60
İbrahim Erez,50,60,40
Süleyman Koçyiğit,100,10,60
Salih Orbay,60,10,30
Şerife Süleymanoğlu,80,30,100
Murat Adal,10,90,100
Osman Aybar,50,20,100
Sude Balcı,60,10,40
Zeynep Koyuncu,50,90,50
İbrahim Pekkan,20,10,60
Fatih Erdoğan,30,60,30
Abdullah Ekşioğlu,40,60,10
Osman Adan,30,90,50
Ramazan Paksüt,90,20,20
Halil Gökgöz,80,10,20
Emre Kurutluoğlu,70,80,100
Mahmut Akışık,40,80,20
Yusuf Hamzaoğlu,100,40,90
Ali Akan,90,90,80
Zeliha Beşerler,100,80,20
Ali Oraloğlu,20,20,90
Hanife Poçan,100,50,10
Ayşe Kurutluoğlu,50,10,80
Fatih Akman,100,10,60
Mehmet Babacan,70,60,6


def not_okuma(satir):

    satir = satir[:-1]

    liste = satir.split(",")

     print(liste)


with open("C:/Users/Doğan Ege BÜLTE/Desktop/Notlar Python .txt","r",encoding = "utf-8") as file:

    for i in file:
        not_okuma(i)

Output():
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
['Doğan Ege BÜLTE', '100', '100', '100']
['Ali Emre ARAR', '1', '2', '3']
['Kelami Batuhan BÖLÜKBAŞI', '100', '90', '100']
['Ali Efe ERDİNÇ', '100', '89', '100']
['Hatice Günday', '70', '90', '20']
['Mustafa Akyürek', '90', '80', '60']
['Ramazan Topaloğlu', '60', '30', '50']
['Elif Akşit', '80', '40', '80']
['Mehmet Düşenkalkar', '70', '20', '40']
['Hatice Dağdaş', '90', '90', '80']
['Merve Tütüncü', '40', '30', '30']
['Hatice Pekkan', '50', '70', '60']
['Merve Alyanak', '70', '60', '30']
['Meryem Aşıkoğlu', '20', '80', '70']
['Süleyman Uluhan', '40', '10', '100']
['Esra Ekici', '10', '10', '30']
['Emine Kumcuoğlu', '90', '30', '80']
['Süleyman Kumcuoğlu', '50', '10', '60']
['Şerife Kumcuoğlu', '40', '70', '70']
['Sude Tekand', '90', '50', '90']
['Elif Nebioğlu', '10', '10', '60']
['Sude Berberoğlu', '10', '100', '50']
['Yasemin Durmaz', '40', '70', '10']
['Fadime Akyürek', '50', '20', '100']
['Fatma Akşit', '60', '40', '90']
['Emre Sözeri', '50', '50', '20']
['Yasemin Kurutluoğlu', '40', '50', '40']
['Fatma Akman', '80', '20', '30']
['Hacer Korol', '80', '50', '90']
['Recep Altınbaş', '40', '70', '80']
['Murat Numanoğlu', '70', '100', '100']
['Fatih Fahri', '40', '10', '10']
['Halil Sarıoğlu', '30', '70', '60']
['Merve Arıcan', '30', '30', '70']
['İsmail Kaplangı', '60', '50', '10']
['Emir Egeli', '80', '20', '80']
['Havva Erbulak', '30', '10', '80']
['Hacer Okumuş', '70', '100', '70']
['Salih Ağaoğlu', '10', '10', '40']
['Zeliha Ağaoğlu', '100', '80', '30']
['Abdullah Solmaz', '60', '40', '50']
['Fatih Elmastaşoğlu', '20', '20', '60']
['Hacer Karaer', '90', '90', '60']
['Sude Kumcuoğlu', '60', '20', '30']
['Abdullah Kuzucu', '100', '40', '40']
['Hanife Söyler', '100', '20', '80']
['Sude Orbay', '60', '30', '40']
['Sultan Uluç', '90', '90', '30']
['Hanife Beşok', '80', '100', '50']
['Hülya Karadaş', '80', '100', '10']
['Fatma Tuğluk', '60', '20', '50']
['Halil Güçlü', '100', '80', '30']
['Recep Eronat', '60', '100', '20']
['Büşra Koyuncu', '60', '70', '70']
['Hüseyin Kunt', '50', '80', '10']
['Halil Numanoğlu', '70', '60', '40']
['Hülya Gürmen', '80', '100', '30']
['Ömer Kulaksızoğlu', '40', '40', '60']
['Zeliha Demirel', '70', '40', '100']
['Mustafa Aşıkoğlu', '60', '70', '90']
['Süleyman Orbay', '90', '80', '60']
['İbrahim Erez', '50', '60', '40']
['Süleyman Koçyiğit', '100', '10', '60']
['Salih Orbay', '60', '10', '30']
['Şerife Süleymanoğlu', '80', '30', '100']
['Murat Adal', '10', '90', '100']
['Osman Aybar', '50', '20', '100']
['Sude Balcı', '60', '10', '40']
['Zeynep Koyuncu', '50', '90', '50']
['İbrahim Pekkan', '20', '10', '60']
['Fatih Erdoğan', '30', '60', '30']
['Abdullah Ekşioğlu', '40', '60', '10']
['Osman Adan', '30', '90', '50']
['Ramazan Paksüt', '90', '20', '20']
['Halil Gökgöz', '80', '10', '20']
['Emre Kurutluoğlu', '70', '80', '100']
['Mahmut Akışık', '40', '80', '20']
['Yusuf Hamzaoğlu', '100', '40', '90']
['Ali Akan', '90', '90', '80']
['Zeliha Beşerler', '100', '80', '20']
['Ali Oraloğlu', '20', '20', '90']
['Hanife Poçan', '100', '50', '10']
['Ayşe Kurutluoğlu', '50', '10', '80']
['Fatih Akman', '100', '10', '60']
['Mehmet Babacan', '70', '60', '6']
"""
"""

def not_okuma(satir):
    satir = satir[:-1]

    liste = satir.split(",")

    isim = liste[0]

    not1 = int(liste[1])

    not2 = int(liste[2])

    not3 = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if (son_not >= 90):

        harf = "AA"

    elif (son_not >= 85):

        harf = "AB"

    elif (son_not >= 80):
        harf = "BB"

    elif (son_not >= 75):

        harf = "BC"

    elif (son_not >= 70):
        harf = "CC"

    elif (son_not >= 65):

        harf = "CD"

    elif (son_not >= 60):
        harf = "DD"

    elif (son_not >= 55):
        harf = "FD"

    else:
        harf = "FF"

    return isim + "------------------->" + harf + "\n"


with open("C:/Users/Doğan Ege BÜLTE/Desktop/Notlar Python .txt", "r", encoding="utf-8") as file:
    eklenecekler_listesi = []

    for i in file:


        eklenecekler_listesi.append(not_okuma(i))

    print(eklenecekler_listesi)

Output():
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
['Doğan Ege BÜLTE------------------->AA\n', 'Ali Emre ARAR------------------->FF\n', 'Kelami Batuhan BÖLÜKBAŞI------------------->AA\n', 'Ali Efe ERDİNÇ------------------->AA\n', 'Hatice Günday------------------->FD\n', 'Mustafa Akyürek------------------->BC\n', 'Ramazan Topaloğlu------------------->FF\n', 'Elif Akşit------------------->CD\n', 'Mehmet Düşenkalkar------------------->FF\n', 'Hatice Dağdaş------------------->AB\n', 'Merve Tütüncü------------------->FF\n', 'Hatice Pekkan------------------->DD\n', 'Merve Alyanak------------------->FF\n', 'Meryem Aşıkoğlu------------------->FD\n', 'Süleyman Uluhan------------------->FD\n', 'Esra Ekici------------------->FF\n', 'Emine Kumcuoğlu------------------->CD\n', 'Süleyman Kumcuoğlu------------------->FF\n', 'Şerife Kumcuoğlu------------------->DD\n', 'Sude Tekand------------------->BC\n', 'Elif Nebioğlu------------------->FF\n', 'Sude Berberoğlu------------------->FF\n', 'Yasemin Durmaz------------------->FF\n', 'Fadime Akyürek------------------->DD\n', 'Fatma Akşit------------------->CD\n', 'Emre Sözeri------------------->FF\n', 'Yasemin Kurutluoğlu------------------->FF\n', 'Fatma Akman------------------->FF\n', 'Hacer Korol------------------->BC\n', 'Recep Altınbaş------------------->CD\n', 'Murat Numanoğlu------------------->AA\n', 'Fatih Fahri------------------->FF\n', 'Halil Sarıoğlu------------------->FF\n', 'Merve Arıcan------------------->FF\n', 'İsmail Kaplangı------------------->FF\n', 'Emir Egeli------------------->DD\n', 'Havva Erbulak------------------->FF\n', 'Hacer Okumuş------------------->BC\n', 'Salih Ağaoğlu------------------->FF\n', 'Zeliha Ağaoğlu------------------->CD\n', 'Abdullah Solmaz------------------->FF\n', 'Fatih Elmastaşoğlu------------------->FF\n', 'Hacer Karaer------------------->BC\n', 'Sude Kumcuoğlu------------------->FF\n', 'Abdullah Kuzucu------------------->FD\n', 'Hanife Söyler------------------->CD\n', 'Sude Orbay------------------->FF\n', 'Sultan Uluç------------------->CD\n', 'Hanife Beşok------------------->CC\n', 'Hülya Karadaş------------------->FD\n', 'Fatma Tuğluk------------------->FF\n', 'Halil Güçlü------------------->CD\n', 'Recep Eronat------------------->FD\n', 'Büşra Koyuncu------------------->CD\n', 'Hüseyin Kunt------------------->FF\n', 'Halil Numanoğlu------------------->FD\n', 'Hülya Gürmen------------------->CD\n', 'Ömer Kulaksızoğlu------------------->FF\n', 'Zeliha Demirel------------------->CC\n', 'Mustafa Aşıkoğlu------------------->BC\n', 'Süleyman Orbay------------------->BC\n', 'İbrahim Erez------------------->FF\n', 'Süleyman Koçyiğit------------------->FD\n', 'Salih Orbay------------------->FF\n', 'Şerife Süleymanoğlu------------------->CC\n', 'Murat Adal------------------->CC\n', 'Osman Aybar------------------->DD\n', 'Sude Balcı------------------->FF\n', 'Zeynep Koyuncu------------------->DD\n', 'İbrahim Pekkan------------------->FF\n', 'Fatih Erdoğan------------------->FF\n', 'Abdullah Ekşioğlu------------------->FF\n', 'Osman Adan------------------->FD\n', 'Ramazan Paksüt------------------->FF\n', 'Halil Gökgöz------------------->FF\n', 'Emre Kurutluoğlu------------------->AB\n', 'Mahmut Akışık------------------->FF\n', 'Yusuf Hamzaoğlu------------------->BC\n', 'Ali Akan------------------->AB\n', 'Zeliha Beşerler------------------->DD\n', 'Ali Oraloğlu------------------->FF\n', 'Hanife Poçan------------------->FF\n', 'Ayşe Kurutluoğlu------------------->FF\n', 'Fatih Akman------------------->FD\n', 'Mehmet Babacan------------------->FF\n']


"""
def not_okuma(satir):
    satir = satir[:-1]

    liste = satir.split(",")

    isim = liste[0]

    not1 = int(liste[1])

    not2 = int(liste[2])

    not3 = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if (son_not >= 90):

        harf = "AA"

    elif (son_not >= 85):

        harf = "AB"

    elif (son_not >= 80):
        harf = "BB"

    elif (son_not >= 75):

        harf = "BC"

    elif (son_not >= 70):
        harf = "CC"

    elif (son_not >= 65):

        harf = "CD"

    elif (son_not >= 60):
        harf = "DD"

    elif (son_not >= 55):
        harf = "FD"

    else:
        harf = "FF"

    return isim + "------------------->" + harf + "\n"


with open("C:/Users/Doğan Ege BÜLTE/Desktop/Notlar Python .txt", "r", encoding="utf-8") as file:
    eklenecekler_listesi = []

    for i in file:


        eklenecekler_listesi.append(not_okuma(i))


with open("C:/Users/Doğan Ege BÜLTE/Desktop/Sınıf Notlama Python.txt", "w", encoding="utf-8") as file2:

    for i in eklenecekler_listesi:

        file2.write(i)