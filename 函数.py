# def print_square(num):
#     for i in range(1,num+1):
#         for j in range(i):
#             print('*', end=" ")
#         print()
#     for i in range(num+1,0,-1):
#         for j in range(i):
#             print('*', end=" ")
#         print()
# def print_square2(num):
#     print_square(num)
#     print()
# print_square2(5)




# def print_square(num):
#     for i in range(num):
#         for j in range(num - i):
#             print(" ", end="")
#         for j in range(i + 1):
#             print("*", end="")
#         print()
#     for i in range(num - 1, -1, -1):
#         for j in range(num - i):
#             print(" ", end="")
#         for j in range(i + 1):
#             print("*", end="")
#         print()

# def print_square2(num):
#     for i in range(num + 1, 0, -1):
#         for j in range(i):
#             print(" ", end="")
#         for j in range(num - i + 1):
#             print("*", end="")
#         print()

# def print_square3(num):
#     print_square(num)
#     # print_square2(num)
#
# print_square3(5)


# def print_square(num):
#     for i in range(num+1):
#         for j in range(num - i+1):
#             print(" ", end="")
#         for j in range(2 * i - 1):
#             print("*", end="")
#         print()
# def print_square2(num):
#     for i in range(2 * num - 1):
#         for j in range(i):
#             print(' ', end="")
#         for j in range((num-i)*2+1):
#             print('*', end="")
#         print()
# def print_square3(num):
#     print_square(num)
#     print_square2(num)
# print_square3(4)



def print_square(num):
    for i in range(1, num + 1):  # 控制行数
        for j in range(num - i):  # 打印前导空格
            print(" ", end="")
        for j in range(2 * i - 1):  # 打印星号
            print("*", end="")
        print()

def print_square2(num):
    for i in range(num - 1, 0, -1):  # 控制行数（倒序）
        for j in range(num - i):  # 打印前导空格
            print(" ", end="")
        for j in range(2 * i - 1):  # 打印星号
            print("*", end="")
        print()

def print_square3(num):
    print_square(num)  # 打印上半部分
    print_square2(num)  # 打印下半部分

print_square3(4)
