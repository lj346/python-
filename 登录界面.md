i=0
sum_jh=2
while i<3:
    name=input("请输入用户名：")
    num=int(input("请输入密码："))
    if name=="lj" and num==123:
        print("登录成功")
        break
    else:
        print(f"登录失败，还有{sum_jh}次机会")
        i+=1
        sum_jh-=1
        if sum_jh<0:
            break
