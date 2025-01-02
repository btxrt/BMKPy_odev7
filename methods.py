from db import urunler

def urun_ekle(isim, fiyat):
    urunler.append({"isim": isim, "fiyat": fiyat})

def urun_guncelle(index, yeni_isim, yeni_fiyat):
    urunler[index] = {"isim": yeni_isim, "fiyat": yeni_fiyat}

def urunleri_getir():
    return urunler