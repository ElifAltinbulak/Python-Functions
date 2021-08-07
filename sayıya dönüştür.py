def gercek_deger(oylar):
    cevap=list()
    degerler=oylar.split()
    for i in degerler:
        if "k" not in i:
            cevap.append(int(i))
        else:
            gercek=i.replace("k","00").replace(".","")
            cevap.append(int(gercek))
    return cevap
print(gercek_deger("6.8k 13.5k 32"))
def fib(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(8))
def apocalyptic(sayı):
    x=str(pow(2,sayı))
    if x.count("666")==0:
        return "Güvenli"
    elif x.count("666")==1:
        return "Tek"
    elif x.count("666")==2:
        return "Çift"
    elif x.count("666")==3:
        return "Üçlü"
print(apocalyptic(931))
def zip(yazi):
    sayı=yazi.count("zip")
    if sayı<2:
        return -1
    else:
        ilk=yazı.find("zip")
        return yazı.find("zip",ilk+1)
a.find("zip",10)#10.indexten sonrasına bakılır
def saklı(yazi):
    liste=yazi.split(" ")
    yeni=list()
    tire=0
    for i in liste:
        if len(i)>2:
            tire=len(i)-2
        else:
            tire=0
        yeni.append(i[0]+"-"*tire+i[-1])
    return " ".join(yeni)




    
