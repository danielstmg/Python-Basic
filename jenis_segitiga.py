# Nama file: jenis_segitiga.py
# Pembuat: Daniel Sahat Parulian Situmeang
# Tanggal: 01 Oktober 2020
# Deskripsi: Menentukan jenis segitiga yang memiliki sisi a,b,c

# Defenisi dan Spesifikasi dari fungsi jenis_segitiga(a,b,c) adalah :
# jenis_segitiga : 3 integer --> string
#    jenis_segitiga(a,b,c) menentukan jenis segitiga dengan sisi a,b,c apakah
#       termasuk ke segitiga sama sisi atau segitiga sama kaki atau segitiga sembarang

# Realisasi
def jenis_segitiga(a,b,c):
    if (( a == b) and (b == c) and (a == c)):
        return ("Segitiga Sama Sisi ")
    if (a != b != c):
        return ("Segitiga Sembarang")
    else:
        return ("segitiga Sama Kaki")

# Aplikasi
print (jenis_segitiga(3,3,3))
print (jenis_segitiga(1,2,3))
print (jenis_segitiga(4,4,6))


