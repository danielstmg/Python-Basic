def integer(a,d,n):
    if n ==0:
        return 0
    else:
        return a + integer(a+d,d,n-1)

# Aplikasi
print(integer(1,1,3))
print(integer(1,3,5))
print(integer(1,1,2))
