# Nama File  : Tabel.py
# Pembuat    : 
# NIM        : 
# Tanggal    : 

# Data Tabel
dataGedung  = ['A','B']
dataHarike1 = [11,22]
dataHarike2 = [33,44]
dataHarike3 = [55,66]
dataHarike4 = [77,88]
dataHarike5 = [99,88]
dataHarike6 = [77,66]
dataHarike7 = [55,44]

# Output
print('''
--------------------------------------------------------------------------------------------------------------
|  Gedung  |  Hari ke-1  |  Hari ke-2  |  Hari ke-3  |  Hari ke-4  |  Hari ke-5  |  Hari ke-6  |  Hari ke-7  |
--------------------------------------------------------------------------------------------------------------''')
for x in range(len(dataGedung)):
    isi = str(dataGedung[x])
    print('|    '+isi,end='')
    for y in range(13-7-len(isi)):
        print(' ',end='')
    isi1 = str(dataHarike1[x])
    print('|      '+isi1,end='')
    for y in range(19-12-len(isi1)):
        print(' ',end='')
    isi2 = str(dataHarike2[x])
    print('|      '+isi2,end='')
    for y in range(19-12-len(isi2)):
        print(' ',end='')
    isi3 = str(dataHarike3[x])
    print('|      '+isi3,end='')
    for y in range(19-12-len(isi3)):
        print(' ',end='')
    isi4 = str(dataHarike4[x])
    print('|      '+isi4,end='')
    for y in range(19-12-len(isi4)):
        print(' ',end='')
    isi5 = str(dataHarike5[x])
    print('|      '+isi5,end='')
    for y in range(19-12-len(isi5)):
        print(' ',end='')
    isi6 = str(dataHarike6[x])
    print('|      '+isi6,end='')
    for y in range(19-12-len(isi6)):
        print(' ',end='')
    isi7 = str(dataHarike7[x])
    print('|      '+isi7,end='')
    for y in range(19-12-len(isi7)):
        print(' ',end='')
    print('|')
print('--------------------------------------------------------------------------------------------------------------')




    
