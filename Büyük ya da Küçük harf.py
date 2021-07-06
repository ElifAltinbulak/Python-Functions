#Büyük ya da Küçük harf mi
def aynı(harf):
    if harf==harf.upper() or harf==harf.lower():
        return "True"
    else:
        return "False"
print(aynı("hello"))
print(aynı("HELLO"))
print(aynı("Hello"))

        
