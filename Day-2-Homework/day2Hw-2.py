# Daha çok nasıl geliştirebileceğimi araştırıp 2.defa aynı projeyi yaptım

ogrenciler = []
while True:
    secim = int(input("İşlemler\n1-Ekle\n2-Ad Soyad ile Sil\n3-Çoklu Ekle\n4-Listele\n5-ID Öprenme\n6-Çoklu Sil\nSeçim:"))
    def ekle(ad,soyad):
        ad = input("Ad: ")
        soyad = input("Soyad: ")
        ogrenciler.append(f"{ad} {soyad}")
        print(ogrenciler)
        return secim
        
    def  degerSil(ad,soyad):
        ad = input("Silinece Ad: ")
        soyad = input("Silinecek Soyad: ")
        ogrenciler.remove(f"{ad} {soyad}")
        listele()

    def cokluEkle():
        sayi = int(input("Eklenecek Öğrenci Sayısını Giriniz: "))
        for i in range(sayi):
            ekle(ad,soyad)
        listele()

    def listele():
        for i in range(len(ogrenciler)):
            print(ogrenciler[i])
            i+=1

    def ogrenciId(ad,soyad):
        ad = input("Ad: ")
        soyad = input("Soyad: ")
        for ogrenci in ogrenciler:
            ogrenci = ogrenciler.index(f"{ad} {soyad}")
        print(f"Öğrenci Numarası: {ogrenci}")

    def cokluSil():
        sayi = int(input("Silmek İstediğiniz Öğrenci Sayısı:  "))
        for i in range(sayi):
            ogrenciler.pop(i)
            i+=1
        listele()

    ad = "Ad: "
    soyad = "Soyad: "
    if secim == 1:
        ekle(ad,soyad)
    elif secim == 2:
        degerSil(ad,soyad)
    elif secim == 3:
        cokluEkle()
    elif secim == 4:
        listele()
    elif secim == 5:
        ogrenciId(ad,soyad)
    elif secim == 6:
        cokluSil()
    elif secim == 7:
        print("Çıkış Yapılıyor...")
        break
    else:
        print("Yanlış Seçim Yaptınız")
        