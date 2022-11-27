# Nama file: konversi_suhu.py
# Pembuat: Daniel Sahat Parulian Situmeang
# Tanggal: 01 Oktober 2020
# Deskripsi: Mengkonversi suhu yang diukur dalam derajat celcius ke derajat
#            reamur, fahrenheit , dan kelvin

# Defenisi dan Spesifikasi dari fungsi konversi_suhu adalah :
# celcius : real --> real
#   celcius(c) merupakan input untuk suhu awal dalam derajat celcius
# reamur : real --> real
#   reamur(r) merupakan konversi dari celcius ke reamur
# fahrenheit : real --> real
#   fahrenheit(f) merupakan konversi dari celcius ke fahrenheit
# kelvin : real --> real
#   kelvin(k) merupakan konversi dari celcius ke kelvin

# Realisasi
def celcius(c):
    return (c)
def reamur(r):
    return (celcius(r)/5*4)
def fahrenheit(f):
    return (celcius(f)*9/5+32)
def kelvin(k):
    return (celcius(k)+273)

# Aplikasi
print("="*10,"Konversi suhu","="*10)
x = float(input("Masukkan suhu dalam celcius:"))
print("="*36)
print("suhu dalam celcius adalah",celcius(x),"derajat celcius")
print("suhu dalam reamur adalah",reamur(x),"derajat reamur")
print("suhu dalam fahrenheit adalah",fahrenheit(x),"derajat fahrenheit")
print("suhu dalam kelvin adalah",kelvin(x),"derajat kelvin")





