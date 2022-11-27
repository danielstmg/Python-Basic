def multi3(n):
    if n ==1:
        return 3
    if n + 1 == n:
        return 3
    else:
        return 3 + multi3(n-1)

# Aplikasi
print(multi3(6))
print(multi3(3))
