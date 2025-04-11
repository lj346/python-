def rabbit(n):
    if n == 0 or n == 1:
        return 1
    else:
        return rabbit(n - 1) + rabbit(n - 2)
months=12
num=rabbit(months)
print(f"一年后共有 {num} 对兔子。")