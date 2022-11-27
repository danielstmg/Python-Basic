# Nama file: pangkat3_v2.py
# Pembuat: Daniel Sahat Parulian Situmeang
# Tanggal: 22 September 2020
# Deskripsi: menghitung nilai pangkat3 dari sebuah masukan integer melalui fungsi antara

# Defenisi dan spesifikasi dari fungsi pangkat3 (versi 2) bernama fx3v2(x) adalah :
# fx3v2 : integer --> integer
#   fx3v2(x) menghitung pangkat tiga dari x, sebuah bilangan integer integer, menggunakan fungsi antara fx2(x)

# fx2 : integer --> integer
#   fx2(x) menghitung pangkat dua dari x, sebuah bilangan integer

# Realisasi
def fx2(x):
    return(x*x)

def fx3v2(x):
    return(x*fx2(x))

# Aplikasi
print (fx3v2(4))
print (fx3v2(4+2))
print (fx3v2(-10))

