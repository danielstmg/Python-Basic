# Nama file: dif.py
# Deskripsi: pembagian dua bilangan bulat
# Pembuat: Daniel Sahat Parulian Situmeang
# Tanggal: 27 Oktober 2020

# DEFENISI DAN SPESIFIKASI
# dif : integer > 0 --> real > 0
#    dif(x,y) membagi x dan y
# dif(x,y) = x / y
#          = 1 + dif(x-y,y)

def dif(x,y):
    if y == 0:
        return 'Tak Terhingga'
    if x == 0:
        return 0
    if x > 0:
        return 1 + dif(x-y,y)
    else:
        return 'input salah'

# Aplikasi
print(dif(4,0))
print(dif(4,1))
print(dif(5,5))
print(dif(10,2))

