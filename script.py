def velocidad_mrua(v0,a,t):
    return v0 + a*t
def posicion_mrua(x0,v0,a,t):
    return x0 + v0*t + (1/2)*a*(t**2)
x0 = 5 #m
v0 = 8 #m/s
a = -2 #m/s**2
for t in range(7):
    x = posicion_mrua(x0,v0,a,t)
    v = velocidad_mrua(v0,a,t)
    if v == 0:
        print("el movil se detuvo a los",t,"segundos")
        print("la posicion del movil es de",x,"m a los",t,"s")
    elif v < 0:
        print("la velocidad es negativa a los",t,"s (se mueve a la izquierda)")
        print("la posicion del movil es de",x,"m a los",t,"s")
    else:
         print("la velocidad del movil es de",v,"m/s a los",t,"s")
         print("la posicion del movil es de",x,"m a los",t, "s")