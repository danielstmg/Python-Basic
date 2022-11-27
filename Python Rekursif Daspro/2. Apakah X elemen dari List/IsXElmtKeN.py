# Nama File : IsXElmtKeN.py
# Pembuat : Daniel Sahat Parulian Situmeang
# Tanggal : 8 November 2020
# Deskripsi : Menentukan apakah X adalah elemen ke-N dari List L dimana N >= 0 ,
#             dan N <= banyaknya elemen list 

# Definisi dan Spesifikasi
#IsXElmtKeX : elemen , integer >= 0 , List(tidak kosong) --> boolean
#     IsXElmtKex(X,N,L) true jika X adalah elemen ke-N dari list L, N >=0 ,dan 
#                       N <= banyaknya elemen list , false jika tidak

#Realisasi
def isEmpty(L):
    return L == []

def firstEl(L):
    return L[0]

def tail(L):
    return L[1:]

def isMember(L,X):
    if isEmpty(L):
        return False
    else:
        if firstEl(L) == X:
            return True
        else:
            return isMember(tail(L),X)

def prec(N):
    return N-1

def IsXElmtKeN(X,N,L):
    if isMember(L,X):
        if N == 1 and firstEl(L) == X:
            return True
        else:
            return False or IsXElmtKeN(X,prec(N),tail(L))
    else:
        return False

#Aplikasi
L = [2,4,6,8,10,12,14,16]

print(IsXElmtKeN(4,5,L))
print(IsXElmtKeN(6,3,L))
print(IsXElmtKeN(7,14,L))