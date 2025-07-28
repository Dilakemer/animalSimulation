from hayvanlar import *
import random
from collections import Counter
import matplotlib.pyplot as plt
import time

# Grafikler için veri toplama yapıları
populasyon_verisi = {
    Tur.KOYUN.value: [],
    Tur.INEK.value: [],
    Tur.TAVUK.value: [],
    Tur.HOROZ.value: [],
    Tur.KURT.value: [],
    Tur.ASLAN.value: [],
    Tur.AVCI.value: []
}
adim_sayilari = []


def populasyon_olustur() -> list[Hayvan]:
    hayvanlar = []
    rng = random.Random()

    # 15 erkek, 15 dişi koyun
    for _ in range(15):
        hayvanlar.append(Koyun(rng.randint(0, 499), rng.randint(0, 499), Cinsiyet.ERKEK))
        hayvanlar.append(Koyun(rng.randint(0, 499), rng.randint(0, 499), Cinsiyet.DISI))

    for _ in range(5):
        hayvanlar.append(Inek(rng.randint(0, 499), rng.randint(0, 499), Cinsiyet.ERKEK))
        hayvanlar.append(Inek(rng.randint(0, 499), rng.randint(0, 499), Cinsiyet.DISI))

    for _ in range(4):
        hayvanlar.append(Aslan(rng.randint(0, 499), rng.randint(0, 499), Cinsiyet.ERKEK))
        hayvanlar.append(Aslan(rng.randint(0, 499), rng.randint(0, 499), Cinsiyet.DISI))

    for _ in range(5):
        hayvanlar.append(Kurt(rng.randint(0, 499), rng.randint(0, 499), Cinsiyet.ERKEK))
        hayvanlar.append(Kurt(rng.randint(0, 499), rng.randint(0, 499), Cinsiyet.DISI))

    for _ in range(10):
        hayvanlar.append(Tavuk(rng.randint(0, 499), rng.randint(0, 499), Cinsiyet.DISI))

    for _ in range(10):
        hayvanlar.append(Horoz(rng.randint(0, 499), rng.randint(0, 499), Cinsiyet.ERKEK))

    # 1 avcı ekleyelim
    hayvanlar.append(Avci(rng.randint(0, 499), rng.randint(0, 499)))
    return hayvanlar


def avlanma_kontrolu(hayvanlar: list[Hayvan]):
    hayvan_kopya = hayvanlar.copy()
    avlanacaklar = set()

    for hayvan in hayvan_kopya:
        if hayvan.Tur == Tur.AVCI:
            for av in hayvan_kopya:
                if av != hayvan and hayvan.mesafe_hesapla(av) <= 8:
                    avlanacaklar.add(av)
        elif hayvan.Tur == Tur.KURT:
            for av in hayvan_kopya:
                if av.Tur in [Tur.KOYUN, Tur.TAVUK, Tur.HOROZ] and hayvan.mesafe_hesapla(av) <= 4:
                    avlanacaklar.add(av)
        elif hayvan.Tur == Tur.ASLAN:
            for av in hayvan_kopya:
                if av.Tur in [Tur.KOYUN, Tur.INEK] and hayvan.mesafe_hesapla(av) <= 5:
                    avlanacaklar.add(av)

    for av in avlanacaklar:
        if av in hayvanlar:
            hayvanlar.remove(av)


def ureme_kontrolu(hayvanlar: list[Hayvan]):
    yeni_hayvanlar = []
    rng = random.Random()

    mevcut_sayilar = Counter(h.Tur for h in hayvanlar)

    max_ureme = {
        Tur.KOYUN: 100,
        Tur.INEK: 30,
        Tur.TAVUK: 50,
        Tur.KURT: 20,
        Tur.ASLAN: 10,
        Tur.HOROZ: 40,
        Tur.AVCI: 0
    }

    ureme_olasikligi = {
        Tur.KOYUN: 0.7,
        Tur.INEK: 0.5,
        Tur.TAVUK: 0.6,
        Tur.KURT: 0.4,
        Tur.ASLAN: 0.3,
        Tur.HOROZ: 0.6,
        Tur.AVCI: 0.0
    }

    for i in range(len(hayvanlar)):
        for j in range(i + 1, len(hayvanlar)):
            hayvan1 = hayvanlar[i]
            hayvan2 = hayvanlar[j]

            if (hayvan1.Tur == hayvan2.Tur and
                    hayvan1.Cinsiyet != hayvan2.Cinsiyet and
                    hayvan1.mesafe_hesapla(hayvan2) <= 3):

                tur = hayvan1.Tur

                if mevcut_sayilar[tur] >= max_ureme.get(tur, float('inf')):
                    continue

                if rng.random() > ureme_olasikligi.get(tur, 0):
                    continue

                orta_x = (hayvan1.KonumX + hayvan2.KonumX) // 2
                orta_y = (hayvan1.KonumY + hayvan2.KonumY) // 2
                cinsiyet = rng.choice(list(Cinsiyet))

                if tur == Tur.KOYUN:
                    yeni_hayvanlar.append(Koyun(orta_x, orta_y, cinsiyet))
                elif tur == Tur.INEK:
                    yeni_hayvanlar.append(Inek(orta_x, orta_y, cinsiyet))
                elif tur == Tur.TAVUK:
                    yeni_hayvanlar.append(Tavuk(orta_x, orta_y, cinsiyet))
                elif tur == Tur.KURT:
                    yeni_hayvanlar.append(Kurt(orta_x, orta_y, cinsiyet))
                elif tur == Tur.ASLAN:
                    yeni_hayvanlar.append(Aslan(orta_x, orta_y, cinsiyet))
                elif tur == Tur.HOROZ:
                    yeni_hayvanlar.append(Horoz(orta_x, orta_y, cinsiyet))

    hayvanlar.extend(yeni_hayvanlar)


def sonuclari_yazdir(hayvanlar: list[Hayvan]):
    sayac = Counter(h.Tur.value for h in hayvanlar)
    print("\n=== SONUÇLAR ===")
    for tur, sayi in sayac.items():
        print(f"{tur}: {sayi}")


def populasyon_verisi_guncelle(hayvanlar: list[Hayvan], adim: int):
    sayac = Counter(h.Tur.value for h in hayvanlar)
    for tur in populasyon_verisi.keys():
        populasyon_verisi[tur].append(sayac.get(tur, 0))
    adim_sayilari.append(adim)


def grafikleri_ciz():
    plt.figure(figsize=(15, 10))

    # Popülasyon eğrileri
    plt.subplot(2, 2, 1)
    for tur, veri in populasyon_verisi.items():
        plt.plot(adim_sayilari, veri, label=tur)
    plt.title('Popülasyon Değişimi')
    plt.xlabel('Adım Sayısı')
    plt.ylabel('Birey Sayısı')
    plt.legend()
    plt.grid(True)

    # Son durum pasta grafiği
    plt.subplot(2, 2, 2)
    son_durum = {tur: veri[-1] for tur, veri in populasyon_verisi.items()}
    plt.pie(son_durum.values(), labels=son_durum.keys(), autopct='%1.1f%%')
    plt.title('Son Popülasyon Dağılımı')

    # Konum dağılımı
    plt.subplot(2, 2, 3)
    konumlar = [(h.KonumX, h.KonumY, h.Tur.value) for h in hayvanlar]
    x, y, tur = zip(*konumlar)
    renkler = {'Koyun': 'green', 'İnek': 'brown', 'Tavuk': 'yellow',
               'Horoz': 'orange', 'Kurt': 'gray', 'Aslan': 'red', 'Avcı': 'black'}
    for t in set(tur):
        mask = [current_tur == t for current_tur in tur]
        plt.scatter([x[i] for i in range(len(x)) if mask[i]],
                   [y[i] for i in range(len(y)) if mask[i]],
                   label=t, c=renkler.get(t, 'blue'), alpha=0.6)
    plt.title('Hayvanların Konum Dağılımı')
    plt.xlabel('X Koordinatı')
    plt.ylabel('Y Koordinatı')
    plt.legend()
    plt.grid(True)

    # Toplam popülasyon eğrisi
    plt.subplot(2, 2, 4)
    toplam = [sum(values) for values in zip(*populasyon_verisi.values())]
    plt.plot(adim_sayilari, toplam, 'k-', linewidth=2)
    plt.title('Toplam Popülasyon Değişimi')
    plt.xlabel('Adım Sayısı')
    plt.ylabel('Toplam Birey Sayısı')
    plt.grid(True)

    plt.tight_layout()
    plt.savefig('populasyon_simulasyonu.png')  # Grafiği dosyaya kaydet
    plt.show()


if __name__ == "__main__":
    hayvanlar = populasyon_olustur()
    print("Başlangıç popülasyonu oluşturuldu!")

    # Başlangıç verisini kaydet
    populasyon_verisi_guncelle(hayvanlar, 0)

    for adim in range(1, 1001):
        t1 = time.time()

        # Hareket
        for hayvan in hayvanlar:
            hayvan.hareket_et()

        # Avlanma
        avlanma_kontrolu(hayvanlar)

        # Üreme (her 10 adımda bir)
        if adim % 10 == 0:
            ureme_kontrolu(hayvanlar)

        # Aşırı popülasyon kontrolü
        if len(hayvanlar) > 50000:
            print(f"🚨 Çok fazla hayvan oluştu ({len(hayvanlar)}). Simülasyon durduruluyor!")
            break

        # Veri güncelleme (her adımda)
        populasyon_verisi_guncelle(hayvanlar, adim)

        # İlerleme göstergesi (her 100 adımda)
        if adim % 100 == 0:
            sure = time.time() - t1
            print(f"✅ Adım {adim} tamamlandı - Toplam hayvan: {len(hayvanlar)} - Bu adımın süresi: {sure:.2f} saniye")

    sonuclari_yazdir(hayvanlar)
    grafikleri_ciz()