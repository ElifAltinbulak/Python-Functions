#harf ve fazlasıyla çevir
def ters(yazi):
    deger=yazi.split()#split liste haline getirir ve bu şekilede döngülere rahatça erişebiliriz
    cevap=""
    for i in deger:
        if len(i)<5:
            cevap += i+" "
        else:
            cevap=i[::-1]+" "
    return cevap.strip()#strip toplar
print(ters("İstanbulu dinliyorum. Gözlerim kapalı..."))
print(ters("Ters"))
yazi="test"
deger=yazi.split()
liste=[int(i) for i in deger]

