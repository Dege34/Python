"""
2. dereceden bir bilinmeyenli denklemin köklerini bulma

Denklem : 2x^2 + bx + c

Deltayı Hesaplama: b**2 - 4* a * c

Birinci Kök : (-b -delta** 0.5) / (2*a)
İkinci Kök : (-b + delta ** 0.5) / (2*a)

"""
"""
int() yazarak hepsini yorum komutuna alıyoruz 
delta normalde matematikte olduğu gibi b²-4ac formülüyle bulunuyor 

"""
a = int(input("x² katsayısı:"))
b = int(input("x katsayısı:"))
c = int(input("c katsayısı:"))

delta = b**2 - 4 * a * c
x1 = (b ** 0.5) / (2 * a)
x2 = (b ** 0.5) / (2 * a)

print("Birinci Kök:  {}\nİkinci Kök:  {}\nDelta:  {}".format(x1,x2,delta))

