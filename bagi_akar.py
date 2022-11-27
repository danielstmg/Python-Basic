# Nama file: bagi_akar.py
# Pembuat: Daniel Sahat Parulian Situmeang
# Tanggal: 01 Oktober 2020
# Deskripsi: Menghitung hasil pembagian antara akar-akar persamaan kuadrat

# Defenisi dan Spesifikasi dari fungsi bagi_akar(x,y,z) adalah :
# x1(a,b,c) : 3 real --> real
#    x1(a,b,c) merupakan akar pertama dari rumus ABC
# x2(a,b,c) : 3 real --> real
#    x2(a,b,c) merupakan akar kedua dari rumus ABC
# bagi_akar(x,y,z) : 3 real --> real
#    bagi_akar(x,y,z) menghitung hasil bagi dari akar-akar x1 dan x2 

# Realisasi
import math

def x1(a,b,c):
    return ((-b)+(math.sqrt (b*b - (4*a*c)))) /(2*a)
def x2(a,b,c):
    return ((-b)-(math.sqrt (b*b - (4*a*c)))) /(2*a)

def bagi_akar(x,y,z):
    if x1(x,y,z) > x2(x,y,z):
        return x1(x,y,z)/x2(x,y,z)
    else:
        return x2(x,y,z)/x1(x,y,z)

# Aplikasi
print("\nHasil pembagian akar-akar dari x^2+2x-15 adalah:\n", bagi_akar(1,2,-15))
print("="*20)
print("Hasil pembagian akar-akar dari x^2+2x-3 adalah:\n", bagi_akar(1,2,-3))
print("="*20)
print("Hasil pembagian akar-akar dari x^2+4x-12 adalah:\n", bagi_akar(1,4,-12))
print("="*20)
print("Hasil pembagian akar-akar dari x^2+5x+6 adalah:\n", bagi_akar(1,5,6))
print("="*20)
print("Hasil pembagian akar-akar dari x^2-5x+6 adalah:\n", bagi_akar(1,-5,6))
print("="*20)

    
