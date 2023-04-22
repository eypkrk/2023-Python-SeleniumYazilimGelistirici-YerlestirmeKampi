                                        ##Phyton Veri Tipleri

Yeni bir kodlama dili öğrenirken ilk öğrenmemiz gereken bu kodlama dilinin veri tipleridir. 
Bende size Phyton kodlama dilinin veri tiplerini açıklayacağım. Phyton’da yaklaşık olarak 6 farklı veri tipi bulunmaktadır. 
Bu veri tiplerini şöyledir;

##Metinsel Veri Tipi
Metinsel veri tipi dediğimiz normal yazı yazmak için kullandığımız veri tipidir. 
-Phyton da bir yazı değeri tanımlayacaksak bunu str ile tanımlıyoruz.

Örnek olarak
x = str(“Merhaba Dünya”)

##Sayısal Veri Tipi
-Sayısal veri tipi dediğimiz rakamlardan, çok büyük sayılardan ve virgüllü sayılardan oluşmaktadır. Phyton da bir rakam 
tanımlayacaksak bunu int ile tanımlıyoruz. 
-Eğer çok büyük bir sayı tanımlamak istersek bunu da complex ile tanımlıyoruz. 
-Bu ikisi haricinde virgüllü bir sayı tanımlamak istersek bunuda float ile tanımlıyoruz. Sırasıyla örnek verecek olursak,
Örnek olarak
x = int(20)
x = complex(1j)
x = float(1.5)

##Dizi Veri Tipi
Phyton kodlama dilinde dizi veri tipi dediğimizde aklımıza gelecek olan şey diziler olmalıdır. Dizi veri tipleri içerisinde 3 tane veri tipi vardır.
-İlk olarak list veri tipinden bahsedeceğim çünkü başlıktan da anlaşılacağı gibi list veri tipi dizi tanımlamaya benziyor. 
List veri tipinin içine istersek string istersek int değerler tanımlayabiliriz. Buda Phyton un esnekliğinden kaynaklanan güzel bir özellik diyebiliriz.
-Daha sonra ki bahsedeceğim veri tipi tuple bu veri tipi bir önce ki bahsettiğimiz list veri tipine çok benzer neredeyse tek fark diyebileceğimiz bu veri tipi sadece okumaya yarar. Yani ekleme yapamayız.
-Son olarak açıklayacağım dizi veri tipi ise range veri tipidir. Bu veri tipinde kullanırken range’e tanımladığımız değerin 0’dan başlayıp yazdığımız değer kadar dönmesini sağlar, ama range’e tanımladığımız yani son sayıyı yazdırmaz.

Örnek olarak
x = [‘abcdef’,34,24.5,’list’]
print(x veya x[0])
x = (‘abcdef’,34,24.5,’tuple’)
range(6)

##Adresleme Veri Tipi
Bu veri tipine örnek olarak dictionary sözlük tipini örnek veriyoruz. 
-Kodlamada kullanımı ise dict olarak kullanılır. Bu veri tipi veri değerlerini çift tutmak için kullanılan bir veri tipidir.

Örnek olarak
x = {‘name’:’Gaziantep’,’code’:’27000’,’dept’:’Bilgisayar Mühendisi’}

##Küme Veri Tipi
Küme veri tipleri biraz dizileri anımsatırlar. Bu veri tiplerine 2 tane örnek vereceğim.
-İlk olarak açıklayacağım veri tipi  set  bu veri tipinin özelliği sıralanamaz bir ver yığınıdır. 
 Veri index sıralaması nasıl ise çıktısı da öyle olur.
-Sırada ki veri tipi ise frozenset’dir Sıralamayı alfabenin tersine bir şekilde yapar.

Örnek olarak
x = {‘muz’, ’armut’,’elma’ }
x = frozenset({{‘muz’, ’armut’,’elma’ })
üstteki çıktı aynı olur. Ama alttaki çıktı alfabenin tersi yönünde sıralanır.

##Mantıksal Veri Tipi
-Mantıksal bir veri tipi olan boolean iki değer sahiptir. Bu değerler true ve false dur. 
 Bunu da doğru ve yanlış olarak açıklayabiliriz.

Örnek olarak
x = True

##Binary Veri Tipi
Binary veri tipine 3 tane örnek vereceğim.
-Bunlardan ilki bytes’dır. Bu veri tipi 0 ve 1 değerlerinden oluşmaktadır. 8’bitlik değer barındırır.
-Sırada ki açıklayacağım veri tipi ise bytearray dir. Bu veri tipi byte veri tipinde oluşturulan  veriler üzerinde 
 değişiklik yapmak için kullanılır.
-Son olarak açıklayacağım veri tipi ise memoryview dir. Bu veri tipi bellek durumunu görüntülemek için kullanılan veri türüdür.

Örnek olarak
x = ”Veri Tipleri”
print(bytes(x,utf-8)) normal çıkıtı verir.
print(bytes(x,utf-32)) normal çıktı vermez.
print(bytearray(x))

Kodlama.io sitesinde ki başlıklar,ödev tanımları, ödev amaçları, açıklama gibi veriler str veri tipi ile oluşmaktadır. 
Kullanıcı adı ve parola da kullanılan karışık veri tiplerinde oluşmaktadır.
Yorum sayıları ve ders sayıları ise int veri tipinden oluşmaktadır.

##if bloğu-1
fullName = input("isim Giriniz: ")

userName = "Eyüp"
password = "12345"
if userName == fullName:
    print("Kullanıcı adı doğrudur.")
else:
    print("Kullanıcı adınızı kontrol ediniz.")
##if bloğu-2
sayi1 = 25
sayi2 = 30

if sayi1 > sayi2:
    print("sayi1 sayi2 den büyüktür.")
elif sayi2 > sayi1:
    print("sayi2 sayi1 den büyüktür")
else
    print("sayi2 sayi1 e eşittir.")