

""" 
Nesne tabanlı programlama 
sınıf(class) ve nesne(object)
"""
#Class nasil tanimlanir, nesne nasil olusturulur?
#Bir onceki programda ogrencilerin bilgilerini girdik fakat hepsi icin ayni bilgileri girmeyebilirdik.
#Mesela bazı ogrencilerin ad,soyad,yas,no bilgisini alirken diger ogrencilerin sadece ad ve soyad bilgilerini alabilirdik. 
#Hepsi icin ayni bilgileri almak zorunlu olsun istiyorsak bunu __init__(self) ile yapariz.
 
class Ogrenci():                               #Ogrenci adnda bir sinif olusturduk.
    def __init__(self,ad="Girilmedi",soyad="Girilmedi",yas="Girilmedi",no="Girilmedi"):        #self her zaman olmak zorundadir.
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.no=no
#Ogr1=Ogrenci()                                #Bu sekilde yaparsak hata aliriz.Bizden 4 tane bilgi girilmesi isteniyor..
Ogr1=Ogrenci("Mahir","Korkmaz",25,"180514126") #Ogr1 adinda Ogrenci nesnesi olusturduk.Bilgileri sirasi ile yazmaya dikkat et!
print(Ogr1.ad)
print(Ogr1.no)

Ogr2=Ogrenci("Hasret","Turk",23,"147878479")
print(Ogr2.ad)
print(Ogr2.yas)

#Peki bu parametreleri eksik girersek ne olur? Hata aliriz..Hata almamak icin asagidaki gibi bir kod yazabiliriz.

"""
class Ogrenci():                               
    def __init__(self,ad="Girilmedi",soyad="Girilmedi",yas="Girilmedi",no="Girilmedi"):    bunu yukariya da yazalim..     
"""

Ogr3=Ogrenci("Melisa","Kartal",no="245615487")      #Burada no'yu belirtmek zorundayiz yoksa yas numara olarak algilanir.
print(Ogr3.soyad)
print(Ogr3.yas)
