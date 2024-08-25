

"""
------------------
Veritabanı nedir ?
-------------------
veritabanı uygulamalarımızda websitelerimizde veya en genel anlamda programlarımızda gerekli olan bilgileri depoladığımız bir yapıdır

Örneğin Facebook'un kullanıcıları gönderileri tuttuğu veritabanları gibi günümüzde kullanılan bazı veritabanı türleri şunlardır;


Relational Database = Sqlite ,Mysql   === Tablolardan oluşur

DocumentBased Database = MongOb ,  === Arzure DocumentDd Dökümanlardan oluşur

**Bizim bu bölümde inceleyeceğimiz veritabanı Sqlite ilişkisel bir veritabanıdır ve bu veritabanı tablolardan oluşur Her bir tablo veritabanında belli gruplanmış verileri tutar.

*Sqlite veritabanı sunucusuz bir veri tabanıdır

*SQL(Structured Query Language)
*daha fazlası için : https://www.w3schools.com/sql/
________________________________________________________________________________________________________________________________________________________________________
import sqlite3 -----------------------> Squlite'ı dahil ediyoruz

con = sqlite3.connect("kütüphane.db") -----------------------> Connection'un kısaltımıdır bağlantıyı başlatır
                                                                ve Tabloya bağlıyoruz eğer böyle bir (kütüphane.db) adında kütüphane yoksa oluşturur ve bağlar
                                                                varsa sadece bağlantı işlemi yapar.


cursor = con.cursor()  -----------------------> Cursor isimli değişken veritabanı üzerinde işlem yapmak için  kullanacağımız bir imleç olacak

cursor.close() -----------------------> Bağlantıyı kapatıyoruz
________________________________________________________________________________________________________________________________________________________________________

Kitaplık Tablosu oluşturma
___________________________________
Veritabanında kitaplık isimli bir tablo oluşturmak için şu 2 sorgudan birini kullanabiliriz
_________________________________________________________________________________________________________
CREATE TABLE kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT,Sayfa Sayısı INT)-Bu sorgu Kitaplık için bir tablo oluşturacak ve bu tablonun özellikleri

İsim TEXT --> String | Yazar TEXT --> String , Yayınevi TEXT --> String,Sayfa Sayısı INT --> int) olacak Ancak bu sorguyu art arda çalıştırırsak
"Tablo Already Exists" hatası alacağız
________________________________________________________________________________________________________________________________________________________________________

CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT,Sayfa Sayısı INT) -Bu sorgu tablo yoksa oluşturacak tablo varsa hata vermeyecektir
******************************************************
Kodlarımız şu şekilde:

import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (Isim TEXT,Yazar TEXT,Yayinevi TEXT,Sayfa_Sayisi INT)")
    con.commit()

tablo_olustur()
con.close()
*********************************************************************************************************************************************************************************
2. Ders ||||||Tablolarla Veri Tabanı
*********************************************************************************************************************************************************************************
Şimdi de kitaplık tablomuza veri eklemeye çalışalım.Çalıştıracağımız sorgu şu olacak:

INSERT INFO kitaplık VALUES("İstanbul Hatırası,Ahmet Ümit,Everest,561")

*************************
NOTE: SQL sorguları küçük veya büyük harfle de yazılabilir.
Örnek olarak:
INSERT INFO kitaplık VALUES("İstanbul Hatırası,Ahmet Ümit,Everest,561")
veya
insert info kitaplık VALUES("İstanbul Hatırası,Ahmet Ümit,Everest,561")
*************************
Kodlarımız şu şekilde:

import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (Isim TEXT,Yazar TEXT,Yayinevi TEXT,Sayfa_Sayisi INT)")
    con.commit()
def veri_ekle():
    cursor.execute("Insert into kitaplik Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()

veri_ekle()

con.close()
*************************
Kodlarımız şu şekilde:
import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (Isim TEXT,Yazar TEXT,Yayinevi TEXT,Sayfa_Sayisi INT)")
    con.commit()
def veri_ekle():
    cursor.execute("Insert into kitaplik Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()
def veri_ekle2(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("Insert into kitaplik Values(?,?,?,?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()

isim = input("isim:")
yazar = input("yazar:")
yayinevi = input("yayinevi:")
sayfa_sayisi = int(input("Sayfa Sayisi:"))

veri_ekle2(isim,yazar,yayinevi,sayfa_sayisi)


con.close()
*********************************************************************************************************************************************************************************
3. Ders ||||||Tablolardaki verileri çekme
*********************************************************************************************************************************************************************************
Önceki derslerimizde Tablo oluşturmayı ve Tabloya veri eklemeyi öğrenmiştik.Bu dersimizde de tablodaki verileri nasıl çebileceğimizi öğrenmeye çalışacağız.
Tablodan veri çekmek için SQL sorgularını kullanacağız.

Select * From kitaplık -------> Tablodan tüm bilgileri almamızı sağlar

Select İsim Yazar From kitaplık ----------------> Tablodan İsim ve Yazar özelliklerini almamızı sağlar

Select * From kitaplık where Yayınevi = "Everest" ----------------> Sadece Yayınevi özelliği Everest olanları alır.
***************************
Örnek
***************************
import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (Isim TEXT,Yazar TEXT,Yayinevi TEXT,Sayfa_Sayisi INT)")
    con.commit()
def veri_ekle():
    cursor.execute("Insert into kitaplik Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()
def veri_ekle2(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("Insert into kitaplik Values(?,?,?,?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()
def verileri_al():
    cursor.execute("Select * From kitaplik")
    liste = cursor.fetchall()
    print("Kitaplik Tablosunun bilgileri:")

    for i in liste:
        print(i)
verileri_al()


con.close()
******************
ÇIKTI
******************
Kitaplik Tablosunun bilgileri:
('İstanbul Hatırası', 'Ahmet Ümit', 'Everest', 561)
('Kavgam', 'Adolf Hitler', 'Nazi Yayýnevi', 560)
('Yüzük Kardesligi', 'J.R.R Tolkien', 'Metis Edebiyat', 486)
('İstanbul HATIRASI', 'EGE', 'AEGE AYAYINCILIK', 21421)
***************************
Örnek
***************************
import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (Isim TEXT,Yazar TEXT,Yayinevi TEXT,Sayfa_Sayisi INT)")
    con.commit()
def veri_ekle():
    cursor.execute("Insert into kitaplik Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()
def veri_ekle2(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("Insert into kitaplik Values(?,?,?,?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()
def verileri_al():
    cursor.execute("Select * From kitaplik")
    liste = cursor.fetchall()
    print("Kitaplik Tablosunun bilgileri:")

    for i in liste:
        print(i)

def isim_yazar_verileri_al():
    cursor.execute("Select Isim,Yazar From kitaplik")
    liste = cursor.fetchall()

    for i in liste:
        print(i)
isim_yazar_verileri_al()


con.close()
******************
ÇIKTI
******************
('İstanbul Hatırası', 'Ahmet Ümit')
('Kavgam', 'Adolf Hitler')
('Yüzük Kardesligi', 'J.R.R Tolkien')
('İstanbul HATIRASI', 'EGE')

***************************
Örnek
***************************
import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (Isim TEXT,Yazar TEXT,Yayinevi TEXT,Sayfa_Sayisi INT)")
    con.commit()
def veri_ekle():
    cursor.execute("Insert into kitaplik Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()
def veri_ekle2(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("Insert into kitaplik Values(?,?,?,?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()
def verileri_al():
    cursor.execute("Select * From kitaplik")
    liste = cursor.fetchall()
    print("Kitaplik Tablosunun bilgileri:")

    for i in liste:
        print(i)

def isim_yazar_verileri_al():
    cursor.execute("Select Isim,Yazar From kitaplik")
    liste = cursor.fetchall()

    for i in liste:
        print(i)

def yayin_evi_al(yayinevi):
    cursor.execute("Select * from kitaplik where Yayinevi = ?",(yayinevi,))

    liste = cursor.fetchall()

    for i in liste:
        print(i)
yayin_evi_al("Everest")


con.close()
******************
ÇIKTI
******************
('İstanbul Hatırası', 'Ahmet Ümit', 'Everest', 561)
*********************************************************************************************************************************************************************************
4. Ders ||||||Tablolardaki verileri Güncelleme ve Silme
*********************************************************************************************************************************************************************************
Bu derste Sqlite veritabanı ile ilgili son olarak verileri güncellemeyi ve silmeyi öğreneceğiz

##################  Veri Güncelleme   ################

Update kitaplik set Yayinevi = "Everest" where Yayinevi = "Doğan Kitap"

*BU KOD SAYESİNDE  Doğan Kitaplar ---------> Everest'e dönüşür

================================
ÖRNEK:
================================
import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (Isim TEXT,Yazar TEXT,Yayinevi TEXT,Sayfa_Sayisi INT)")
    con.commit()
def veri_ekle():
    cursor.execute("Insert into kitaplik Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()
def veri_ekle2(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("Insert into kitaplik Values(?,?,?,?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()
def verileri_al():
    cursor.execute("Select * From kitaplik")
    liste = cursor.fetchall()
    print("Kitaplik Tablosunun bilgileri:")

    for i in liste:
        print(i)

def isim_yazar_verileri_al():
    cursor.execute("Select Isim,Yazar From kitaplik")
    liste = cursor.fetchall()

    for i in liste:
        print(i)

def yayin_evi_al(yayinevi):
    cursor.execute("Select * from kitaplik where Yayinevi = ?",(yayinevi,))

    liste = cursor.fetchall()

    for i in liste:
        print(i)

def verileri_guncelle(eski_yayinevi,yeni_yayinevi):

    cursor.execute("Update kitaplik set Yayinevi = ? where Yayinevi = ?",(yeni_yayinevi,eski_yayinevi))

    con.commit()
#Commit komutu verileri güncellemede ,veritabanýna bir sey eklemek istedigimizde kullaniriz

verileri_guncelle("Metis Edebiyat","Nazi Yayinevi")

verileri_al()

con.close()
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&6&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&6
Verileri Silme
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&6
Delete From kitaplik where Yazar = "Ahmet Ümit" ----------------> Yazarı Ahmet Ümit olan kitapları tablodan  siler
-----------------------------------------
ÖRNEK :
--------------------------------------
import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (Isim TEXT,Yazar TEXT,Yayinevi TEXT,Sayfa_Sayisi INT)")
    con.commit()
def veri_ekle():
    cursor.execute("Insert into kitaplik Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()
def veri_ekle2(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("Insert into kitaplik Values(?,?,?,?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()
def verileri_al():
    cursor.execute("Select * From kitaplik")
    liste = cursor.fetchall()
    print("Kitaplik Tablosunun bilgileri:")

    for i in liste:
        print(i)

def isim_yazar_verileri_al():
    cursor.execute("Select Isim,Yazar From kitaplik")
    liste = cursor.fetchall()

    for i in liste:
        print(i)

def yayin_evi_al(yayinevi):
    cursor.execute("Select * from kitaplik where Yayinevi = ?",(yayinevi,))

    liste = cursor.fetchall()

    for i in liste:
        print(i)

def verileri_guncelle(eski_yayinevi,yeni_yayinevi):

    cursor.execute("Update kitaplik set Yayinevi = ? where Yayinevi = ?",(yeni_yayinevi,eski_yayinevi))

    con.commit()
#Commit komutu verileri güncellemede ,veritabanýna bir sey eklemek istedigimizde kullaniriz

def verileri_sil(yazar):
    cursor.execute("Delete From kitaplik where Yazar = ?",(yazar,))
    con.commit()

verileri_sil("Ahmet Ümit")

verileri_al()

con.close()

"""







"""
•••••••••••••••CON.EXECUTE("") KOMUTLARI•••••••••••••••••

1•CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT , Sayfa_Sayısı INT) 

Tablo oluşturma execute'u

2•Select İsim,Yazar From kitaplık 
•••••
Select * From kitaplık 

3•Update kitaplık set Yayınevi = 'Everest' where Yayınevi = 'Doğan Kitap'

4•Delete From kitaplık where Yazar = 'Ahmet Ümit

5•INSERT INTO kitaplik VALUES("ZERT","ZART","ZORT",23)

"""







