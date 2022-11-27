# Nama file: date.py
# Deskripsi: membuat tipe bentukan pecahan beserta konstruktor dan selektornya
# Pembuat: Daniel Sahat Parulian Situmeang
# Tanggal: 10 Oktober 2020

# DEFENISI DAN SPESIFIKASI TYPE
# type Date: <Hr: integer 1...31, Bln: integer 1...12, Thn: integer>0>
#   {<Hr,Bln,Thn> adalah sebuah tanggal(Date), dengan Hr adalah Hari, Bln adalah Bulan, dan Thn adalah Tahun.}
# Realisasi dalam python
class Date:
    def __init__(self,h,b,t):
        self.a = h
        self.b = b
        self.c = t

# DEFENISI DAN SPESIFIKASI SELEKTOR
# Hr: integer --> integer
# Hr(D) memberikan hari pada Date D
# Realisasi dalam python
def Hr(D):
    return D.a

# Bln: integer --> integer
# Bln(D) memberikan Bulan pada Date D
# Realisasi dalam python
def Bln(D):
    return D.b

# Thn: integer --> integer
# Thn(D) memberikan Tahun pada Date D
# Realisasi dalam python
def Thn(D):
    return D.c

# DEFENISI DAN SPESIFIKASI KONSTRUKTOR
# MakeDate : 3 integer --> integer
# MakeDate(Hr,Bln,Thn) adalah sebuah tanggal(Date), dengan Hr adalah Hari, Bln adalah Bulan, dan Thn adalah Tahun.
def MakeDate(D):
    return Hr(D)>0 and Hr(D)<=31 and Bln(D)>0 and Bln<=12 and Thn(D)>0

# DEFINISI DAN SPESIFIKASI OPERATOR/FUNGSI LAIN TERHADAP DATE
# NextDay : Date --> Date
#   {NextDay(D) menentukan tanggal setelah Date D}
# Realisasi dalam python
def NextDay(D):
    if Bln(D)==2 and IsKabisat(D):
        if Hr(D)==29:
            return(1,Bln(D)+1,Thn(D))
        else:
            return(1+Hr(D),Bln(D),Thn(D))
    elif Bln(D)==(4 or 6 or 9 or 11):
        if Hr(D)==30:
            return(1,Bln(D)+1,Thn(D))
        else:
            return(1+Hr(D),Bln(D),Thn(D))
    elif Bln(D)==12:
        if Hr(D)==31:
            return(1,Bln(D),Thn(D)+1)
        else:
            return(1+Hr(D),Bln(D),Thn(D))
    else:
        if Hr(D)==31:
            return(1,Bln(D)+1,Thn(D))
        else:
            return(1+Hr(D),Bln(D),Thn(D))

# Yesterday : Date --> Date
#   {Yesterday(D) menentukan tanggal sebelum Date D}
# Realisasi dalam python
def Yesterday(D):
    if Hr(D) != 1:
        return(Hr(D)-1,Bln(D),Thn(D))
    else:
        if Bln(D)==1:
            return(31,12,Thn(D)-1)
        elif Bln(D)==3:
            if IsKabisat(D):
                return(29,2,Thn(D))
            else:
                return(28,2,Thn(D))
        elif (Bln(D) == 5) or (Bln(D) == 7) or (Bln(D) == 10) or (Bln(D) ==12):
            return(30,Bln(D)-1,Thn(D))
        else:
            return(31,Bln(D)-1,Thn(D))

# NextNDay : Date, integer --> Date
#   {NextNDay(D) menentukan tanggal N hari setelah tanggal Date D}
# Realisasi dalam python
def NextNday(D,N):
    return KonversiDayToDate(KonversiDateToDay(D)+N)

# HariKe1900 : Date --> integer
#   {HariKe1900(D) menghitung jumlah hari dari 1 januari 1900 ke Date D}
# Realisasi dalam python
def HariKe1900(D):
    if Bln(D)>2 and IsKabisat(D):
        return(1 + Hr(D) + Month(D) + (Thn(D) - 1900)*365 + Jumlah_Kabisat(D))
    else:
        return(Hr(D) + Month(D) + (Thn(D) - 1900)*365 + Jumlah_Kabisat(D))

# PREDIKAT
# IsEqD : 2 Date --> boolean
#   {IsEqD(D1,D2) menentukan apakah Date D1 sama dengan Date D2}
# Realisasi dalam python
def IsEqD(D1,D2):
    return KonversiDateToDay(D1)==KonversiDateToDay(D2)

# IsEqD : 2 Date --> boolean
#   {IsEqD(D1,D2) menentukan apakah Date D1 sebelum Date D2}
# Realisasi dalam python
def IsBefore(D1,D2):
    return KonversiDateToDay(D1)<KonversiDateToDay(D2)

# IsAfter : 2 Date --> boolean
#   {IsAfter(D1,D2) menentukan apakah Date D1 sesudah Date D2}
# Realisasi dalam python
def IsAfter(D1,D2):
    return KonversiDateToDay(D1)>KonversiDateToDay(D2)

# IsKabisat : Date --> boolean
#   {IsKabisat(D) menentukan apakah Thn(D) adalah tahun kabisat}
# Realisasi dalam python
def IsKabisat(D):
    return Thn(D)%4 == 0

# Jumlah_Kabisat : Date --> integer
#   {Jumlah_Kabisat(D) menentukan jumlah tahun kabisat dari tahun 1900 sampai ke Date D}
# Realisasi dalam python
def Jumlah_Kabisat(D):
    return (Thn(D)-1900)//4

# Month : Date --> integer
#   {Month(D) mengubah bulan ke hari}
# Realisasi dalam python
def Month(D):
    return(0 if Bln(D)==1 else 31 if Bln(D)==2 else 59 if Bln(D)==3 else 90 if Bln(D)==4 else 120 if Bln(D)==5 else 151 if Bln(D)==6 else 181 if Bln(D)==7 else 212 if Bln(D)==8 else 243 if Bln(D)==9 else 273 if Bln(D)==10 else 304 if Bln(D)==11 else 334)

# KonversiDateToDay : Date --> integer
#   {KonversiDateToDay(D) mengubah Date ke hari}
# Realisasi dalam python
def KonversiDateToDay(D):
    return(Hr(D)+Month(D)+Thn(D)*365)

# KonversiDayToDate: integer --> Date
#   {KonversiDayToDate(D) mengubah hari ke Date}
# Realisasi dalam python
def KonversiDayToDate(x):
    if (x % 365)>0 and (x % 365)<=31:
        return(x % 365,1,x // 365)
    elif (x % 365)>31 and (x % 365)<=59:
        return(x % 365 - 31,2,x // 365)
    elif (x % 365)>59 and (x % 365)<=90:
        return(x % 365 - 59,3,x // 365)
    elif (x % 365)>90 and (x % 365)<=120:
        return(x % 365 - 90,4,x // 365)
    elif (x % 365)>120 and (x % 365)<=151:
        return(x % 365 - 120,5,x // 365)
    elif (x % 365)>151 and (x % 365)<=181:
        return(x % 365 - 151,6,x // 365)
    elif (x % 365)>181 and (x % 365)<=212:
        return(x % 365 - 181,7,x // 365)
    elif (x % 365)>212 and (x % 365)<=243:
        return(x % 365 - 212,8,x // 365)
    elif (x % 365)>243 and (x % 365)<=273:
        return(x % 365 - 243,9,x // 365)
    elif (x % 365)>273 and (x % 365)<=304:
        return(x % 365 - 273,10,x // 365)
    elif (x % 365)>304 and (x % 365)<=334:
        return(x % 365 - 304,11,x // 365)
    else:
        return(x % 365 - 334,12,x // 365)

# 4Aplikasi
D1 = Date(1,1,2000)
D2 = Date(2,1,2000)
print(IsKabisat(D1))
print(NextDay(D1))
print(Yesterday(D1))
print(KonversiDateToDay(D1))
print(NextNday(D1,1000))
print(HariKe1900(D1))
print(IsEqD(D1,D2))
print(IsBefore(D1,D2))
print(IsAfter(D1,D2))
