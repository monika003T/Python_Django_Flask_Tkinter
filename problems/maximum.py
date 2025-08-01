#maximum of two no. def maxi(a,b,c
def maxi(a, b, c):
    if a>b and a>c:
        print("a is maximum", a)
    elif b>a and b>c:
        print("b is maximum",b)

    else:
        print("c is maximum", c)
maxi(10,20,30)