# Nama file: apakah_valid.py
# Pembuat: Daniel Sahat Parulian Situmeang
# Tanggal 23 September 2020
# Deskripsi: Mengecek kebenaran dari bilangan yang lebih kecil dari 5
#            atau lebih besar dari 500

# Defenisi dan spesifikasi dari fungsi IsValid(x) adalah :
# IsValid : integer --> boolean
#   IsValid(x) benar jika (x) bernilai lebih kecil dari 5 atau
#              lebih besar dari 500

# Realisasi
def IsValid(x):
    return x < 5 or x > 500

# Aplikasi
print (IsValid(5))
print (IsValid(0))
print (IsValid(500))
print (IsValid(1000))
