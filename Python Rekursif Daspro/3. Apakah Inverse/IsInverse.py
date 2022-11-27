# Nama File : IsInverse.py
# Pembuat : Daniel Sahat Parulian Situmeang
# Tanggal : 8 November 2020
# Deskripsi : Menentukan apakah L2 adalah list dengan urutan elemen terbalik dibandingkan L1,
#             dengan perkataan lain adalah hasil inverse dari L1 

# Definisi dan Spesifikasi
# IsInverse : 2 List --> boolean
#     IsInverse(L1,L2) True jika L2 adalah list dengan urutan elemen terbaik dibandingkan L1,
#                      dengan perkataan lain adalah hasil inverse dari L1

#Realisasi
def isEmpty(L):
    return L == []

def firstEl(L):
    return L[0]

def lastEl(L):
    return L[-1]

def tail(L):
    return L[1:]

def head(L):
    return L[:-1]

def NbEl(L):
    if isEmpty(L):
        return 0
    else:
        return 1+NbEl(tail(L))

def isInverse(L1,L2):
    if NbEl(L1) == NbEl(L2):
        if isEmpty(L1) and isEmpty(L2):
            return True
        else:
            return firstEl(L1) == lastEl(L2) and isInverse(head(tail(L1)),head(tail(L2)))
    else:
        return False

#Aplikasi
L1 = [1,2,3,4,5]
L2 = [5,4,3,2,1]
L3 = [3,2,1,2]
L4 = [3,5,4,1,2]

print(isInverse(L1,L2))
print(isInverse(L1,L4))
print(isInverse(L2,L3))