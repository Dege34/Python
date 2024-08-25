print("""
******************************************************************************

Kullanıcı Girişi:

*******************************************************************************

""")

sys_kullanıcıadı = "Dege36"
sys_kullanıcıparolası = "D$ege2004"

kullanıcı_adı = input("Kullanıcı Adı:")
parola = input("Parola:")

if kullanıcı_adı == kullanıcı_adı and sys_kullanıcıparolası != parola:
    print("Parola Hatalıdır.")

elif kullanıcı_adı != kullanıcı_adı and sys_kullanıcıparolası == parola:
    print("Kullanıcı Adı Hatalıdır..")

elif kullanıcı_adı != kullanıcı_adı and sys_kullanıcıparolası != parola:
    print("Kullanıcı Adı Hatalıdır..")

else:
    print("Hoş geldin ADMİN")

