#Type Point
class point :
    def __init__ (self,w,x,y,z):
        self.a = w
        self.b = x
        self.c = y
        self.d = z

# Selektor
def absis1(P):
    return P.a

def ordinat1(P):
    return P.b

def absis2(P):
    return P.c

def ordinat2(P):
    return P.d

# Konstuktor
def makepoint(P):
    return (absis1(P),ordinat1(P)) + tuple(['dan']) + (absis2(P),ordinat2(P))

# Operator dan Predikat
def gradien(P):
    return (ordinat2(P)-ordinat1(P)) / (absis2(P)-absis1(P))

def issejajar(P1,P2):
    if gradien(P1)==gradien(P2):
        return gradien(P1)==gradien(P2)
    else :
        return gradien(P1)==gradien(P2)

def istegaklurus(P1,P2):
    if gradien(P1)*gradien(P2) == (-1) :
        return gradien(P1)*gradien(P2) == (-1)
    else :
        return gradien(P1)*gradien(P2) == (-1)

# Aplikasi
G1 = point(3,5,2,8)
G2 = point(2,7,5,8)
print('---Titik (x1,y1) dan (x2,y2)---')
print(makepoint(G1))
print('-----Gradien di kedua titik----')
print(gradien(G1))
print(gradien(G2))
print('----------Tipe Boolean---------')
print(issejajar(G1,G2))
print(istegaklurus(G1,G2))
