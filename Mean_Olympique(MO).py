# Nama file: Mean_Olympique.py
# Pembuat: Daniel Sahat Parulian Situmeang
# Tanggal: 22 September 2020
# Deskripsi: Menghitung rata rata dari dua buah bilangan integer, yang bukan
#            maksimum dan bukan minimum dari empat buah integer

# Defenisi dan spesifikasi dari fungsi MO(u,v,w,x) adalah :
# MO : 4 integer >= 0 --> real
#  MO(u,v,w,x) menghitung rata rata dari dua buah bilangan integer,
#  yang bukan maksimum dan bukan minimum dari 4 buah integer :
#  (u+v+w+x-min4 (u,v,w,x)-max4 (u,v,w,x))/2

# max4 : 4 integer > 0 --> integer
#  max4(i,j,k,l) menentukan maksimum dari 4 buah bilangan integer

# min4 : 4 integer > 0 --> integer
#  min4(i,j,k,l) menentukan minimum dari 4 buah bilangan integer

# max2 : 2 integer > 0 --> integer
#  max2(a,b) menentukan makimum dari 2 bilangan integer, hanya dengan
#  ekspresi aritmatika : jumlah dari kedua bilangan ditambah dengan selisih
#  kedua bilangan, hasilnya dibagi 2

# min2 : 2 integer > 0 --> integer
#  min2(a,b) menentukan minimum dari 2 bilangan integer, hanya dengan
#  ekspresi aritmatika : jumlah dari kedua bilangan dikurang dengan selisih
#  kedua bilangan, hasilnya dibagi 2

# Realisasi
def max2(a,b):
    return((a+b) + abs(a-b)) / 2

def min2(a,b):
    return((a+b) - abs(a-b)) / 2

def max4(i,j,k,l):
    return max2((max2(i,j)), max2(k,l))

def min4(i,j,k,l):
    return min2((min2(i,j)), min2(k,l))

def MO(u,v,w,x):
    return ((u+v+w+x) - min4(u,v,w,x) - max4(u,v,w,x)) / 2

# Aplikasi
print (MO(8,12,10,20))
print (MO(2,4,6,8))
print (MO(1,3,5,7))

           


