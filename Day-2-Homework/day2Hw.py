# Bu öğrenci kayıt sistemine;

# Aldığı isim soy isim ile listeye öğrenci ekleyen
# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
# Listeye birden fazla öğrenci eklemeyi mümkün kılan
# Listedeki tüm öğrencileri tek tek ekrana yazdıran
# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
# fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

# Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.


ogrenciler = ["Mehmet Aydın","Ahmet Kısa", "Hayri Karanlık"]
topluOgr = []

def listele():
    for ogrenci in ogrenciler:
        print(ogrenci)

def ekle(ad,soyad):
    ogrenciler.append(f"{ad} {soyad}")#tek ekleme
    print(ogrenciler)

def topluEkle(sayi,ad,soyad):
    i = 0
    sayi = int(input("Eklenecek Öğrenci Sayisi"))
    for i in range(sayi):
        ad = input("Ad: ")
        soyad = input("Soyad: ")
        ekle(ad,soyad)#toplu ekleme

def sil(ad,soyad):
    ad = input("Silinecek ad: ")
    soyad = input("Silinecek soyad: ")
    ogrenciler.remove(f"{ad} {soyad}")#değer ile silme
    print(ogrenciler)

def idListele(ad,soyad):
    i = 0
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    for ogrenci in ogrenciler:#tek tek listeleyen
        if ogrenci == f"{ad} {soyad}":
            print(f"No: {i} - {ogrenci}")
            break
        i+=1
def topluSil(sayi):
    i=0
    while i < int(sayi):
        ogrenciler.pop(i)
        i+=1
    print(ogrenciler)

print("*********Öğrenci Listeleme************")
listele() 
print("*********Öğrenci Ekleme************")
ad = input("İsim Giriniz: ")
soyad = input("Soyad Giriniz: ")
ekle(ad,soyad)
print("*********Değer Silerek Öğrenci Listeleme************")
sil(ad,soyad)
print("*********Öğrenci ID Listeleme************")
idListele(ad,soyad)
sayi = input("Silinecek Öğrenci Sayısını Giriniz: ")
print("*********Toplu Öğrenci Sil************")
topluSil(sayi)
print("*********Toplu Öğrenci Ekle************")
topluEkle(sayi,ad,soyad)
listele()
