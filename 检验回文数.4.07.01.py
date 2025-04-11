def sum_num(number):
    num_1=str(number)
    if num_1==num_1[::-1]:
        return 1
    else:
        return 0
user_input=int(input("请输入一个整数："))
if sum_num(user_input):
    print(f"{user_input} 是回文数")
else:
    print(f"{user_input} 不是回文数")