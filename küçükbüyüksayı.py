#boşluklara göre tam sayıları ayıran en büyük ve en küçük tam sayıları string olarak döndüren bir fonksiyon
def buyuk_kucuk(deger):
    yeni=deger.split()
    yeni=[int(i) for i in yeni]
    buyuk=max(yeni)
    kucuk=min(yeni)
    return str(buyuk),str(kucuk)
print(buyuk_kucuk("3 1 4 6 -1 12"))
