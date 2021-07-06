#çarpanlar
def carpanlar(sayı):
    liste=[]
    for i in range(1,sayı+1):
        if sayı%i==0:
            liste.append(i)
    return liste
print(carpanlar(12))
print(carpanlar(4))
print(carpanlar(17))
