# Nama file: is_origin.py
# Pembuat: Daniel Sahat Parulian Situmeang
# Tanggal: 22 September 2020
# Deskripsi: mengecek apakah dua buah nilai integer (x,y) mewakili titik origin (0,0)

# Defenisi dan spesifikasi dari fungsi apakah origin bernama is_origin(x,y) adalah :
# is_origin : 2 real --> boolean
#   is_origin(x,y) benar jika (x,y) adalah dua nilai yang mewakili titik origin (0,0)

# Realisasi
def is_origin(x,y):
    return (x == 0) and (y == 0)

# Aplikasi
print (is_origin(0,0))
print (is_origin(4.2,0.0))
print (is_origin(2,1))

