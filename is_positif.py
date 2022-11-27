# Nama file: is_positif.py
# Pembuat: Daniel Sahat Parulian Situmeang
# Tanggal: 22 September 2020
# Deskripsi: Mengecek kebenaran dari sebuah bilangan integer apakah bilangan
#            tersebut bernilai positif atau negatif

# Defenisi dan spesifikasi dari fungsi IsPositif?(x) adalah
# IsPositif? : integer --> bolean
#   IsPositif?(x) benar jika x bernilai positif

# Realisasi
def IsPositif(x):
    return x >= 0

# Aplikasi
print (IsPositif(4))
print (IsPositif(-7))
print (IsPositif(10))

