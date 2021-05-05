
""" 
Nesne tabanlı programlama 
sınıf(class) ve nesne(object)
"""
#Class nasil tanimlanir, nesne nasil olusturulur?

class Ogrenci():         #Burada ogrenci sınıfı olusturduk.
    pass

Ogr1=Ogrenci()         #Burada Ogr1 bir nesnedir.
print(Ogr1)            #Bu kodu nesne tanımlamadan calistirmaya calissaydik hata alirdik.

Ogr1.ad="Tugba"
Ogr1.soyad="Kirac"
Ogr1.Yas=21
Ogr1.No="190802014"

print(Ogr1.ad)

Ogr2=Ogrenci()

Ogr2.ad="Sila"
Ogr2.soyad="Nur"
Ogr2.Yas=24
Ogr2.No="190789207"

print(Ogr2.ad)