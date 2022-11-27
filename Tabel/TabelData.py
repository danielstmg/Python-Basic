# Nama File  : TabelData.py
# Pembuat    : Daniel Sahat Parulian Situmeang
# NIM        : 24060120140051
# Tanggal    : 27 November 2020

# Permasalahan 
#    Membuat program untuk mengisi dan menampilkan tabel yang berisi
# jumlah peserta yang hadir pada event diesnatalis kampus yang diadakan 
# selama seminggu full di 2 gedung yang berbeda

# Penyelasaian
# Memakai algoritma pemrograman python 

# Input
a = input("Masukkan Nama Gedung:")
c = int(input("Masukkan data hari ke-1 : "))
e = int(input("Masukkan data hari ke-2 : "))
g = int(input("Masukkan data hari ke-3 : "))
i = int(input("Masukkan data hari ke-4 : "))
k = int(input("Masukkan data hari ke-5 : "))
m = int(input("Masukkan data hari ke-6 : "))
o = int(input("Masukkan data hari ke-7 : "))
b = input("Masukkan Nama Gedung: ")
d = int(input("Masukkan data hari ke-1 : "))
f = int(input("Masukkan data hari ke-2 : "))
h = int(input("Masukkan data hari ke-3 : "))
j = int(input("Masukkan data hari ke-4 : "))
l = int(input("Masukkan data hari ke-5 : "))
n = int(input("Masukkan data hari ke-6 : "))
p = int(input("Masukkan data hari ke-7 : "))

# Data Tabel
dataGedung  = [a,b]
dataHarike1 = [c,d]
dataHarike2 = [e,f]
dataHarike3 = [g,h]
dataHarike4 = [i,j]
dataHarike5 = [k,l]
dataHarike6 = [m,n]
dataHarike7 = [o,p]

# Output
print('''
----------------------------------------------------------------------------------------------------------------
|   Gedung   |  Hari ke-1  |  Hari ke-2  |  Hari ke-3  |  Hari ke-4  |  Hari ke-5  |  Hari ke-6  |  Hari ke-7  |
----------------------------------------------------------------------------------------------------------------''')
for x in range(len(dataGedung)):
    isi = str(dataGedung[x])
    print('|  '+isi,end='')
    for y in range(13-3-len(isi)):
        print(' ',end='')
    isi1 = str(dataHarike1[x])
    print('|     '+isi1,end='')
    for y in range(19-11-len(isi1)):
        print(' ',end='')
    isi2 = str(dataHarike2[x])
    print('|     '+isi2,end='')
    for y in range(19-11-len(isi2)):
        print(' ',end='')
    isi3 = str(dataHarike3[x])
    print('|     '+isi3,end='')
    for y in range(19-11-len(isi3)):
        print(' ',end='')
    isi4 = str(dataHarike4[x])
    print('|     '+isi4,end='')
    for y in range(19-11-len(isi4)):
        print(' ',end='')
    isi5 = str(dataHarike5[x])
    print('|     '+isi5,end='')
    for y in range(19-11-len(isi5)):
        print(' ',end='')
    isi6 = str(dataHarike6[x])
    print('|     '+isi6,end='')
    for y in range(19-11-len(isi6)):
        print(' ',end='')
    isi7 = str(dataHarike7[x])
    print('|     '+isi7,end='')
    for y in range(19-11-len(isi7)):
        print(' ',end='')
    print('|')
print('----------------------------------------------------------------------------------------------------------------')




    
