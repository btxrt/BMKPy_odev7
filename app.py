from methods import urun_ekle, urun_guncelle, urunleri_getir

def main():
    urun_ekle("iPhone 15", 60000)
    urun_guncelle(0, "iPhone 15 Pro", 80000)
    for urun in urunleri_getir():
        print(f"Ürün Adı: {urun['isim']}, Fiyat: {urun['fiyat']}")

if __name__ == "__main__":
    main()