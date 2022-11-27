# Nama file: subs.py
# Deskripsi: pengurangan dua bilangan bulat
# Pembuat: Daniel Sahat Parulian Situmeang
# Tanggal: 27 Oktober 2020

# DEFENISI AN SPESIFIKASI
# subs : 2 integer > 0 --> integer > 0
#     subs(x,y) mengurangkan x dan y
# subs(x,y) = x - y
#           = subs(x,y-1) - 1

def subs(x,y):
    if x == y:
        return 0
    if y == 0:
        return x
    else:
        return subs(x,y-1) - 1

# Aplikasi
print(subs(4,0))
print(subs(4,1))
print(subs(5,5))



