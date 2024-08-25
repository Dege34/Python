class Dosya():

    def __init__(self):
        with open("C://Users/Doğan Ege BÜLTE/Desktop/ödevvv.txt.txt","r",encoding="utf-8") as file:
            okuma = file.read()

            kelimeler = okuma.split()

            self.sade_kelimeler = list()

        for i in kelimeler:

            i = i.strip("")
            i = i.strip(".")
            i = i.strip(",")
            i = i.strip('."')

            self.sade_kelimeler.append(i)

    def tumkelimeler(self):

        kelime = set()

        for i in self.sade_kelimeler:
            kelime.add(i)

            print(i)
            print("---------------------------------------------")


dosya = Dosya()

dosya.kelime_frekansi()