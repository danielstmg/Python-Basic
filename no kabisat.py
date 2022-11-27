# Nama file: Harike1900nokabisat.py
# Pembuat: Daniel Sahat Paruluan Situmeang
# Tanggal: 01 Oktober 2020
# Deskripsi: Menentukan penanggalan tanpa memperhitungkan tahun kabisat

# Defenisi dan Spesifikasi dari fungsi Harike1900(d,m,y) adalah :
# Harike1900nokabisat : integer[1..31], integer[1..12],integer[0..99] -->
#                       integer [1..366]
#   Harike1900(d,m,y) dari suatu tanggal <d,m,y> adalah hari 'absolut'
#       dihitung mulai 1 Januari 1900+y.1 Januari tahun 1900+y adalah hari ke-1
# dpm : integer [1..12] --> integer[1..36]
#   dpm(B) adalah jumlah hari pada tahun ybs pada tanggal 1 bulan B. Terhitung
#      mulai satu januari: kumulatif jumlah hari dari tanggal 1 januari s/d
#      tanggal 1 bulan B, tanpa memperhitungkan tahun kabisat

# Realisasi
def Harike1900(d,m,y):
    return (d-1) + dpm(m) + (y*0)
  
def dpm(B):
    if (B == 1):
        return 1
    if (B == 2):
        return 32
    if (B == 3):
        return 60
    if (B == 4):
        return 91
    if (B == 5):
        return 121
    if (B == 6):
        return 152
    if (B == 7):
        return 182
    if (B == 8):
        return 213
    if (B == 9):
        return 244
    if (B == 10):
        return 274
    if (B == 11):
        return 305
    elif(B == 12):
        return 335


#Aplikasi
print (Harike1900(1,1,1))
print (Harike1900(3,4,93))
    
    

    

    
    
    
