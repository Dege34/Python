with open("C://Users//Doğan Ege BÜLTE//Desktop//futbolcular.txt", "r+", encoding="utf-8") as file:
    gs_liste = list()

    bjk_liste = list()

    fener_liste = list()
    for satir in file:

        satir = satir[:-1]

        satir_eleman = satir.split(",")

        isim = satir_eleman[0]

        takim = satir_eleman[1]

        if takim == "Galatasaray":
            gs_liste.append(isim + "\n")
        elif takim == "Fenerbahçe":
            fener_liste.append(isim + "\n")
        elif takim == "Beşiktaş":
            bjk_liste.append(isim + "\n")

    with open("C://Users//Doğan Ege BÜLTE//Desktop//gs.txt", "w", encoding="utf-8") as file_gs:
        for i in gs_liste:
            file_gs.write(i)

    with open("C://Users//Doğan Ege BÜLTE//Desktop//fb.txt", "w", encoding="utf-8") as file_fb:
        for i in fener_liste:
            file_fb.write(i)
    with open("C://Users//Doğan Ege BÜLTE//Desktop//bjk.txt", "w", encoding="utf-8") as file_bjk:
        for i in bjk_liste:
            file_bjk.write(i)

