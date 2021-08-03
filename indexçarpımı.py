def index_carpici(liste):
    sonuc=0
    for i in range(len(liste)):
        sonuc+=liste[i]*i
    return sonuc
print(index_carpici([-2, 4, 10, 7, -9]))
