def say(yazi):
    stoplam,htoplam=0,0
    i=yazi.lower()
    harf=set("abcçdefgğhıijklmnoöprsştuüvyz")
    sayı=set("0123456789")
    for j in i:
        if j in harf:
            htoplam+=1
        elif j in sayı:
            stoplam+=1
    return {"Harfler":htoplam,"Sayılar": stoplam}
print(say("Güzel İstanbul"))
