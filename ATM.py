#Bankamatik
hesaptakipara = 2000

print("BANKAMATİK'E HOŞGELDİNİZ, HANGİ İŞLEMİ YAPACAKSINIZ?")
print("1 : Para Çekme")
print("2 : Para Yatırma")
print("3 : Kart Bilgileri")
print("4 : Kart İade")

işlem = int(input("İşlem Seçiniz:"))
print(işlem)

if işlem == 4:
    print("Kartı iade aldınız ATM'den ayrılabilirsiniz")

if işlem == 1:
     print("Hesabınızdaki para:", hesaptakipara)
     çekilenpara = int(input("Çekmek istediğiniz miktarı giriniz:"))
     kalanpara = (hesaptakipara - çekilenpara)
     if çekilenpara > hesaptakipara:
         print("Yetersiz Bakiye XD")

     if çekilenpara < hesaptakipara:
         print("Kalan Miktar:")
         print(hesaptakipara - çekilenpara)

if işlem == 2:
         yatırılacakpara = int(input("Yatıracağınız miktarı giriniz:"))
         print("Yeni mevcut miktar:")
         print(hesaptakipara+yatırılacakpara)

if işlem == 3:
    print("Kart bilgileri:")
print("-------------")
print("Agah Yusuf Heren")
print("IBAN: 123123213213")


