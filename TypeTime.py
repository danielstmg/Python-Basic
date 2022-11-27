# Type Time
class time :
    def __init__ (self,j,m,d):
        self.x = j
        self.y = m
        self.z = d
    
# Selektor
def hour(P):
    if 0 <= P.x <= 24 :
        return P.x

def minute(P):
    if 0 <= P.y <= 59 :
        return P.y

def second(P):
    if 0 <= P.z <= 59 :
        return P.z

# Konstruktor
def maketime(P):
    return hour(P),minute(P),second(P)

# Predikat
def isbefore(P1,P2):
    if hour(P1)==hour(P2) :
        if minute(P1)==minute(P2):
            return second(P1)<second(P2)
        elif minute(P1)<minute(P2):
            return minute(P1)<minute(P2)
        elif minute(P1)>minute(P2):
            return minute(P1)>minute(P2)
    else :
        return hour(P1)<hour(P2)

def isafter(P1,P2):
    if hour(P1)==hour(P2) :
        if minute(P1)==minute(P2):
            return second(P1)>second(P2)
        elif minute(P1)<minute(P2):
            return minute(P1)>minute(P2)
        elif minute(P1)>minute(P2):
            return minute(P1)>minute(P2)
    elif hour(P1)>hour(P2):
        return hour(P1)>hour(P2)
    elif hour(P1)<hour(P2):
        return hour(P1)>hour(P2)
   
# Operator
def convertsec2time(P):
    if P <= 86400 :
        return (P // 3600),((P%3600) // 60),((P%3600) % 60)
    else :
        return  ((P%86400) // 3600),(((P%86400)%3600) // 60),(((P%86400)%3600) % 60)

def time2sec(P):
    e = hour(P)*3600
    f = minute(P)*60
    g = second(P)
    return e + f + g

def Addtime(P1,P2):
    h = time2sec(P1) + time2sec(P2)
    return convertsec2time(h)

def Addtimedetik(P1,detik):
    i = time2sec(P1) + detik
    return convertsec2time(i)

# Aplikasi
time1 = time (1,20,59)
time2 = time (1,20,58)

print('---Type Boolean---')
print(isbefore(time1,time2))
print(isafter(time1,time2))
print('-----Operator-----')
print(convertsec2time(86401))
print(Addtime(time1,time2))
print(Addtimedetik(time1,400000000))


