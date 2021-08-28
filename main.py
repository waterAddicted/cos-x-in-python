
def cosinus(x,eps):
    t=1
    k=float(0)
    s=float(0)  
    while abs(t)>eps:
        print(t)
        s = s + t
        t = t*((-x*x)/((k*2+1)*(k*2+2)))
        k += 1
    return s

x=float(input())
eps=0.000001
print("cosinus de",x,"este",float(cosinus(x,eps)))