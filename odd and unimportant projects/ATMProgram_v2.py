print("""
*****************************************
*
* *
*  *
*   *   ******* ********   *********
*    *  **      **         **
*     * ******* **         ********
*    *  **      **     *** **
*   *   **      **       * **
*  *    ******* ********** ********
* *
*
------------------------------------------
Dege BANK Atm Makinesine Hoş Geldiniz

1.Para Sorgulama

2.Para Çekme 

3.Para Gönderme

4.Borç Yatırma

5.Döviz Hesabı

6.PROGRAMDAN ÇIK

*****************************************
""")

normal_para = 10000

doviz_hesap = 2000

borc = -200

while True:
    ques1_process = int(input("Lütfen Bir işlem seçiniz:"))
    if ques1_process == 6:
        print("DEGE Bank'ı tercih ettiğiniz için\nTeşekkür Ederiz...")
        break
    if (ques1_process == 2):
        cekilen_para = int(input("Çekmek İstediğiniz Tutarı Girin:"))
        if (normal_para < cekilen_para):
            print("Hesabınızda Yeterli Para Bulunmamaktadır\nHesaptaki Para: {}".format(normal_para))
            continue
        else:
            print("Kalan paranız {}".format(normal_para-cekilen_para))


    if (ques1_process == 1):
        print("Hesaptaki NORMAL Paranız : {}₺\nHesaptaki Döviziniz : {}$\nAktif Borcunuz: {}₺".format(normal_para,doviz_hesap,-borc))

    if (ques1_process == 4):
        print("Şu Anki Aktif Borcunuz {}".format(-borc))
        borc_yatır = int(input("Ne Kadar Yatıracağınızı Yazın:"))
        if borc_yatır < -borc:
            print("Aktif Borcunuz {} TL Kalmıştır".format(borc + borc_yatır))
        else:
            print("Aktif Borcunuz Kalmamıştır Ek olarak {} TL Yatırdığınız için 7 iş gününde Hesabınıza geri aktarılacaktır.".format(borc+borc_yatır))
    if (ques1_process == 3):
        gonderilecek_iban = int(input("Lütfen Para Göndermek istediğiniz 11 Haneli IBAN'ı Girin:"))
        gonderilecek_para = int(input("Lütfen Göndermek İstediğiniz Miktarı Seçin:"))
        if len(str(gonderilecek_iban)) >= 12:
            print("Lütfen 11 Haneli IBAN giriniz")
            break
        iban_emin = int(input("TR{} Hesabına {} TL Göndermek istediğinizden Emin misiniz ?\n1:Evet\t2:Hayır\n".format(gonderilecek_iban,gonderilecek_para)))
        if (iban_emin == 1):
            print("TR{} Hesabına {} Tl Gönderildi Teşekkürler".format(gonderilecek_iban,gonderilecek_para))
        else:
            continue
    if (ques1_process == 5):
        print("Hesabınınızda {}$ Var".format(doviz_hesap))
        continue


