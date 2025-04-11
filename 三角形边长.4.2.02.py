def print_sin(a,b,c):
    if (a + b>c) and (a + c>b) and (c + b>a):
        return 1
    else:
        return 0
while(1):
    a = float(input("请输入第一条边的长度:"))
    b = float(input("请输入第二条边的长度:"))
    c = float(input("请输入第三条边的长度:"))
    if print_sin(a,b,c):
        print("这三个数字可以构成一个三角形。")
    else:
        print("这三个数字不可以构成一个三角形。")
    out = input("退出输入0，继续输入1：")
    if out == '0':
        break