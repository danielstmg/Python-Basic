# Nama file: wujud_air.py
# Pembuat: Daniel Sahat Parulian Situmeang
# Tanggal: 01 oktober 2020
# Deskripsi: Menentukan wujud air yang dicek dari temperatur air dalam derajat
#            celcius dan pada tekanan 1 atm

# Defenisi dan Spesifikasi dari fungsi wujud_air(x) adalah :
# wujud_air :  integer --> string
#   wujud_air(x)menetukan wujud air pada saat temperatur (x) derajat celcius pada
#               tekanan 1 atm

# Realisasi
def wujud_air(x):
    if (x < 0):
        return ("Wujud Es")
    if (0 < x < 100):
        return ("Wujud Cair")
    else:
        return ("Wujud Uap")

# Aplikasi
print (wujud_air(-1))
print (wujud_air(50))
print (wujud_air(100))
    
