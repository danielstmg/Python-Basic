def geo(a,n,s):
    if s ==0:
        return a
    else:
        return geo(a*n,n,s-1)

# Aplikasi
print(geo(1,3,1))
print(geo(1,3,5))
print(geo(1,3,3))



