# Nama file: Least_Square.py
# Pembuat: Daniel Sahat Parulian Situmeang
# Tanggal: 23 September 2020
# Deskripsi: Menentukan jarak dari kedua titik pada Koordinat Cartesius
#            (x1,y1) , (x2,y2)

# Defenisi dan spesifikasi dari fungsi LS(x1,y1,x2,y2) adalah :
# LS : 4 real --> real
#  LS(x1,y1,x2,y2) adalah jarak antara dua buah titik (x1,y1) dengan (x2,y2)

# dif2 : 2 real --> real
#  dif2(x,y) adalah kuadrat dari selisih antara x dan y

# FX2 : real --> real
#  FX2(x) adalah hasil kuadrat dari x

# Realisasi
import math

def FX2(x):
    return x * x

def dif2(x,y):
    return FX2(x - y)

def LS(x1,y1,x2,y2):
    return math.sqrt(dif2(x1,x2) + dif2(y1,y2))

# Aplikasi
print (LS(0,1,0,2))
print (LS(2,3,4,5))
print (LS(0,0,0,0))

       




