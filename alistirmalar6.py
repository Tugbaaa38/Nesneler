

#Metodlar
#class icinde yazilan fonksiyonlara metod denir.

class Ogrenci():                             
    def __init__(self,ad="Girilmedi",soyad="Girilmedi",yas="Girilmedi",no="Girilmedi"):   
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.no=no
   
    def bilgileriGoster(self):
        return print(" Ogrenci ad:{}\n Ogrenci soyad:{}\n Ogrenci yas:{}\n Ogrenci no:{}\n".format(self.ad,self.soyad,self.yas,self.no))
    def YasDegistir(self,Dyas):
        self.yas=Dyas
Ogr1=Ogrenci("Can","Huseyin",22,"14784566521")

Ogr1.bilgileriGoster()

Ogr2=Ogrenci("Toprak","Su",19)
Ogr2.YasDegistir(20)
Ogr2.bilgileriGoster()
