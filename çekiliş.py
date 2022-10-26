import random
#metin="qwertyuıopğüasdfghjklşizxcvbnmöç"
#upper=metin.upper()
#metin2=random.choices(metin,k=50)
#metin2="".join(metin2)
liste=[]
print("Çekilişi başlatmak İçin 'başlat',\n İptal Etmek İçin 'iptal' Yaz.")

while True:
  try:
    
    giris=input("Çekilişe katılacak kişilerin isimlerini yazın: ")
    if giris=="iptal":
      sor=input("Kişiyi mi iptal edeceksiniz (kisi),Yoksa çekilişi mi? (cekilis) \n :")
      if sor=="kisi":
        sor1=input("Kimi iptal etmek istiyorsun?\n ")
        if sor1 in liste:
          yer=liste.index(sor1)
          liste.pop(yer)
          print("Kişiyi çekilişten İptal Ettik.")
          print(liste)
        else:
          print("Böyle biri çekilişte Yok.")
          print(liste)

      elif sor=="cekilis":
        try:
          while True:
            liste.pop()
        except:
          print("Çekiliş İptal edildi.")
    elif giris=="başlat":
      sor3=input("Kazanacak kişi sayısını yazınız :")
      
      sor2=int(sor3)
      sonuc=random.sample(liste, sor2)

      if len(liste)<=sor2 :
       print("Kazanacak Kişi sayısı üye sayısından sayısından fazla olamaz! ")
       print("Tekrar dene!")
      

      else:
       print("Kazananlar:",sonuc)      
    else:
      liste.append(giris)
  except:
   
    if len(liste)<sor2:
        print("kişi sayısından fazla değer girdin tekrar dene")
    else:
     print("hatalı yazdınız")


