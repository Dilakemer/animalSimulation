from enum import Enum
import math
import random


class Cinsiyet(Enum):
    ERKEK = "Erkek"
    DISI = "Dişi"


class Tur(Enum):
    KOYUN = "Koyun"
    INEK = "İnek"
    TAVUK = "Tavuk"
    HOROZ = "Horoz"
    KURT = "Kurt"
    ASLAN = "Aslan"
    AVCI = "Avcı"


class Hayvan:
    def __init__(self, x: int, y: int, cinsiyet: Cinsiyet):
        self.KonumX = x
        self.KonumY = y
        self.Cinsiyet = cinsiyet
        self.Tur = None


    def hareket_et(self):
        self.KonumX += random.randint(-self.HareketBirimi, self.HareketBirimi)
        self.KonumY += random.randint(-self.HareketBirimi, self.HareketBirimi)
        # Sınır kontrolü (500x500 alan)
        self.KonumX = max(0, min(499, self.KonumX))
        self.KonumY = max(0, min(499, self.KonumY))

    def mesafe_hesapla(self, diger_hayvan) -> float:
        return math.sqrt((self.KonumX - diger_hayvan.KonumX) ** 2 +
                         (self.KonumY - diger_hayvan.KonumY) ** 2)


class Koyun(Hayvan):
    def __init__(self, x: int, y: int, cinsiyet: Cinsiyet):
        super().__init__(x, y, cinsiyet)
        self.Tur = Tur.KOYUN
        self.HareketBirimi = 2

class Kurt(Hayvan):
    def __init__(self,x:int,y:int,cinsiyet:Cinsiyet):
        super().__init__(x,y,cinsiyet)
        self.Tur=Tur.KURT
        self.HareketBirimi= 3

class Inek(Hayvan):
    def __init__(self,x:int,y:int,cinsiyet:Cinsiyet):
        super().__init__(x,y,cinsiyet)
        self.Tur=Tur.INEK
        self.HareketBirimi= 2

class Tavuk(Hayvan):
    def __init__(self,x:int,y:int,cinsiyet:Cinsiyet):
        super().__init__(x,y,cinsiyet)
        self.Tur=Tur.TAVUK
        self.HareketBirimi= 1

class Horoz(Hayvan):
    def __init__(self,x:int,y:int,cinsiyet:Cinsiyet):
        super().__init__(x,y,cinsiyet)
        self.Tur=Tur.HOROZ
        self.HareketBirimi= 1

class Aslan(Hayvan):
    def __init__(self,x:int,y:int,cinsiyet:Cinsiyet):
        super().__init__(x,y,cinsiyet)
        self.Tur=Tur.ASLAN
        self.HareketBirimi= 4

# Avcı sınıfı örneği:
class Avci(Hayvan):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, Cinsiyet.ERKEK)
        self.Tur = Tur.AVCI
        self.HareketBirimi = 1