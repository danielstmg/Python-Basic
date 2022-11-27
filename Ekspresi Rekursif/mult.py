# Nama file: mult.py
# Deskripsi: perkalian dua bilangan bulat
# Pembuat: Daniel Sahat Parulian Situmeang
# Tanggal: 27 Oktober 2020

# DEFENISI DAN SPESIFIKASI
# mult : 2 integer > 0 --> integer > 0
#     mult(x,y) mengalikan x dan y
#mult(x,y) = x * y
#          = x + mult(x, y-1)

def mult(x,y):
    if y == 1:
        return x
    if y == 0:
        return 0
    else:
        return x + mult(x, y-1)
    
    
# Aplikasi
print(mult(4,0))
print(mult(4,1))
print(mult(5,5))


