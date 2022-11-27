# Nama file: pecahan.py
# Deskripsi: membuat tipe bentukan pecahan
# Pembuat: Daniel Sahat Parulian Situmeang
# Tanggal: 10 Oktober 2020

# DEFENISI DAN SPESIFIKASI TYPE
# type pecahan : <n : integer >=0, d: integer >0 >
# ( <n: integer >=0, d:integer >0 >, n adalah pembilang (numerator) dan d adalah
#       penyebut (denumerator). Penyebut sebuah pecahan tidak boleh 0(nol) )

# DEFENISI DAN SPESIFIKASI SELEKTOR DENGAN FUNGSI
# pemb : Pecahan --> integer >=0
#     (pemb(p) memberikan numerator pembilang n dari pecahan tersebut)
# Realisasi dalam python
def pemb(p):
    return p.n

# peny : Pecahan --> integer >=0
#     (peny(p) memberikan denumerator penyebut d dari pecahan tersebut)
# Realisasi dalam python
def peny(p):
    return p.d

# DEFENISI DAN SPESIFIKASI KONSTRUKTOR
# MakeP : integer >=0 ,integer >0 --> Pecahan
#     (MakeP(x,y) membentuk sebuah pecahan dari pembilang x dan penyebut y,
#    dengan x dan y integer)
# Realisasi dalam python
class Pecahan:
    def __init__(self, a, b):
        self.n = a
        self.d = b

# DEFENISI DAN SPESIFIKASI OPERATOR TERHADAP PECAHAN
# ( ==Operator aritmatika Pecahan== )
# AddP : 2 Pecahan --> Pecahan
#    (AddP(p1,p2) Menambahkan 2 buah pecahan P1 dan P2 :
#   n1/d1 + n2/d2 = (n1*d2 + n2*d1)/d1*d2 )
# Realisasi dalam python
def AddP(p1,p2):
    return Pecahan(pemb(p1)*peny(p2) + pemb(p2)*peny(p1) , peny(p1)*peny(p2))

# SubP : 2 Pecahan --> Pecahan
#     (SubP(p1,p2) Mengurangkan 2 buah pecahan p1 dan p2 :
#   n1/d1 - n2/d2 = (n1*d2 - n2*d1)/d1*d2 )
# Realisasi dalam python
def SubP(p1,p2):
    return Pecahan(pemb(p1)*peny(p2) - pemb(p2)*peny(p1) , peny(p1)*peny(p2))

# MulP : 2 Pecahan --> Pecahan
#     (MulP(p1,p2) Mengalikan 2 buah pecahan p1 dan p2 :
#   n1/d1 * n2/d2 = (n1 * n2)/(d1 * d2) )
# Realisasi dalam python
def MulP(p1,p2):
    return Pecahan(pemb(p1)*pemb(p2) , peny(p1)*peny(p2))

# DivP : 2 Pecahan --> Pecahan
#     (DivP(p1,p2) Membagi 2 buah pecahan p1 dan p2 :
#    n1/d1 / n2/d2 = (n1*d2)/(d1*n2))
# Realisasi dalam python
def DivP(p1,p2):
    return Pecahan(pemb(p1)*peny(p2) , peny(p1)*pemb(p2))

# RealP : Pecahan --> Real
#     (Menuliskan bilangan pecahan dalam notasi desimal)
# Realisasi dalam python
def RealP(p):
    return pemb(p)/peny(p)

# DEFENISI DAN SPESIFIKASI PREDIKAT
# ( ==Operator relasional Pecahan== )
# IsEqP? : 2 Pecahan --> boolean
#     (IsEqP?(p1,p2) true jika p1 = p2)
#     {Membandingkan apakah 2 buah pecahan sama nilainya:
#    n1/d1 = n2/d2 jika dan hanya jika n1d2 = n2d1 }
# Realisasi dalam python
def IsEqP(p1,p2):
    return (pemb(p1)*peny(p2) == peny(p1)*pemb(p2))

# IsLtP? : 2 Pecahan --> boolean
#      (IsLtP?(p1,p2) true jika p1 < p2)
#      {Membandingkan 2 buah pecahan, apakah p1 lebih kecil nilainya dari p2:
#     n1/d1 < n1/d2 jika dan hanya jika n1d2 < n2d1 }
# Realisasi dalam python
def IsLtP(p1,p2):
    return (pemb(p1)*peny(p2) < peny(p1)*pemb(p2))

# IsGtP? : 2 Pecahan --> boolean
#      (IsGtP(p1,p2) true jika p1 > p2)
#      {Membandingkan 2 buah pecahan, apakah p1 lebih besar nilainya dari p2:
#     n1/d1 > n2/d2 jika dan hanya jika n1d2 > n2d1 }
# Realisasi dalam python
def IsGtP(p1,p2):
    return (pemb(p1)*peny(p2) > peny(p1)*pemb(p2))


# Aplikasi
p1 = Pecahan(3,4)
p2 = Pecahan(1,4)
p3 = AddP(p1,p2)
p4 = SubP(p1,p2)
p5 = MulP(p1,p2)
p6 = DivP(p1,p2)

print(pemb(p1))
print(peny(p2))
print(" ",pemb(p3))
print(" ",peny(p3))
print(pemb(p4))
print(peny(p4))
print(" ",pemb(p5))
print(" ",peny(p5))
print(pemb(p6))
print(peny(p6))
print(RealP(p1))
print(IsEqP(p1,p2))
print(IsLtP(p1,p2))
print(IsGtP(p1,p2))

    
