
gercek_deger = float(input("Gerçek değeri giriniz: "))
olculen_deger = float(input("Ölçülen değeri giriniz: "))

mutlak_hata = abs(gercek_deger - olculen_deger)
bagil_hata = mutlak_hata / gercek_deger
yuzdelik_hata = bagil_hata * 100

virgul_sayisi = int(input("Sonucu virgülden sonra kaç hane kullanmak istersiniz? "))

print(f"Mutlak hata: {mutlak_hata:.{virgul_sayisi}f}")
print(f"Bağıl hata: {bagil_hata:.{virgul_sayisi}f}")
print(f"Yüzdelik hata: {yuzdelik_hata:.{virgul_sayisi}f}%")
