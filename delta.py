def delta(a,b,c):
    return f"""Denklem Sisteminiz: {a}x²+{b}x+{c}
Delta : {b**2-(4*a*c)}"""
print(delta(1,2,2))

def tepenoktası(a,b,c):
    return f"""Denklem Sisteminiz: {a}x²+{b}x+{c}
Tepe Noktası: {-(b/(2*a))}"""
print(tepenoktası(1,2,2))
