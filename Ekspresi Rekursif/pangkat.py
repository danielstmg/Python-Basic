# Nama file: pangkat.py
# Deskripsi: perpangkatan sebuah bilangan integer
# Pembuat: Daniel Sahat Parulian Situmeang
# Tanggal: 27 Oktober 2020

# DEFENISI DAN SPESIFIKASI
# pangkat : integer > 0 --> integer > 0
#    pangkat(x,b) memangkatkan bilangan x dengan pangkatnya adalah b
# pangkat(x,b) = x^b
#              = x * pangkay(x,b-1)

def pangkat(x,b):
    if b == 1:
        return x
    if b == 0:
        return 1
    else:
        return x * pangkat(x,b-1)

# Aplikasi
print(pangkat(4,0))
print(pangkat(4,1))
print(pangkat(5,5))
print(pangkat(5,2))

