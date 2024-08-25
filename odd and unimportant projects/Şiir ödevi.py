"""
class Dosya():

    def satirbas(self):
        with open("C://Users/Doğan Ege BÜLTE/Desktop/şiir.txt","r",encoding="utf-8") as file:

            okunacak = file.read()



            kelimeler = okunacak.split()

            kelimelerin_bas_harfleri = list()

            for i in kelimeler:
                kelimelerin_bas_harfleri.append(i[0])

                for i in kelimelerin_bas_harfleri:
                    if i.isupper() == True:
                        print(i)

                    else:
                        pass



dosya = Dosya()

dosya.satirbas()
"""



