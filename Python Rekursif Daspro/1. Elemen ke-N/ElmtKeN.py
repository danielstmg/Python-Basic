# Nama File : ElmtKeN.py
# Pembuat : Daniel Sahat Parulian Situmeang
# Tanggal : 8 November 2020
# Deskripsi : Menghasilkan elemen ke-N dari list L, dimana
#             dimana N >= 0 dan N <= banyaknya elemen list

# Definisi dan Spesifikasi
# ElmtKeN : integer >= ,List tidak kosong --> elemen
#     ElmtKeN(N,L) menghasilkan elemen ke-N list L, N >= 0 dan 
#                  N <= banyaknya elemen list

#Realisasi
def firstEl(L):
    return L[0]

def tail(L):
    return L[1:]


def prec(N):
    return N-1

def ElmtKeN(N,L):
    if N == 1:
        return firstEl(L)
    else:
        return ElmtKeN(prec(N),tail(L))

#Aplikasi
L1 = [1,2,3,4,'bunga',6]
L2 = [2,3,5,'raya',9]

print(ElmtKeN(2,L1))
print(ElmtKeN(2,L2))
print(ElmtKeN(5,L1))
print(ElmtKeN(4,L2))