#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GÖLGEYE CEZA KESEN BELEDİYE — Çekirdek Motor v0.0.1
Kaldırımda izinsiz uzayan gölgelere idari para cezası keser.
Bilimsel dayanak: Gölge, ışığın tembelliğidir.
"""

import random
import datetime
from textwrap import dedent

CEZA_MADDELERI = [
    "Kaldırım İşgali Yönetmeliği md. 7/G: Gölge, şahsın rızası olmadan kaldırıma uzanamaz.",
    "Güneş Işığı Kullanım Hakkı Kanunu geçici md. 12: Gölge, ışığın ruhsatı olmadan kopyalanamaz.",
    "Belediye Zabıtası Genelgesi 44-B: Gölge, kedi değildir; kedi olsa bile vergi öder.",
    "Estetik Kent Silüeti Tüzüğü: Eğri gölge, şehri çirkinleştirir.",
]

BAHANELER = [
    "Güneş çok dikti, ben ne yapayım?",
    "Ben gölge değilim, karanlık sanatçısıyım.",
    "Sahibim kısa, ben uzun doğdum.",
    "Bu bir protesto, ışık hegemonisine karşı.",
    "Avukatım var, adı Ay.",
]

def ceza_hesapla(gölge_uzunlugu_metre: float) -> float:
    # Resmi tarife: metre başına 17.50 TL + rastgele “estetik zarar”
    temel = gölge_uzunlugu_metre * 17.50
    estetik = random.choice([0, 3.14, 42, 88.8])
    return round(temel + estetik, 2)

def tutanak(ad_soyad: str, gölge_uzunlugu: float) -> str:
    madde = random.choice(CEZA_MADDELERI)
    bahane = random.choice(BAHANELER)
    tutar = ceza_hesapla(gölge_uzunlugu)
    tarih = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    no = random.randint(100000, 999999)
    return dedent(f"""
    ============================================================
         T.C. HAYALÎ BELEDİYESİ  — ZABITA TUTANAĞI
                    Gölge Denetim Şubesi
    ============================================================
    Tutanak No     : GB-{no}
    Tarih          : {tarih}
    Muhatap        : {ad_soyad}
    Suçun Türü     : İzinsiz gölge uzatma / kaldırım işgali
    Gölge Boyu     : {gölge_uzunlugu:.2f} metre
    Dayanak        : {madde}
    Şüphelinin ifadesi: “{bahane}”
    İdari para cezası: {tutar:.2f} TL
    
    Not: Gölge itiraz ederse güneşe dilekçe yazılsın.
    Ödeme yeri: En yakın gölge bankası (şu an kapalı).
    ============================================================
    """).strip()

def main():
    print("GÖLGEYE CEZA KESEN BELEDİYE — interaktif zabıta terminali")
    print("(Ctrl+C ile gölge gibi kaybolabilirsiniz)\n")
    ad = input("Gölgenin sahibinin adı soyadı: ").strip() or "Meçhul Vatandaş"
    try:
        boy = float(input("Gölgenin yerdeki uzunluğu (metre): ") or "1.80")
    except ValueError:
        boy = 1.80
        print("(Anlaşılamadı, varsayılan 1.80 m — ortalama Türk gölgesi)")
    print()
    print(tutanak(ad, boy))
    print()
    print("Uyarı: Bu yazılım gerçek bir belediye değildir. Gölgeniz güvende.")
    # gizli not: herkesin gölgesi aynı güneşin altında uzar; kimin gölgesi daha uzun tartışması şehri ısıtmaz.

if __name__ == "__main__":
    main()
