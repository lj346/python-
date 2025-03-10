"""
sum of consumption 消费金额
Points 积分
grade of membership 会员等级
"""
consumption = float(input("请输入消费金额（元）："))
Points = int(input("请输入积分（分）："))
if consumption>=1000 and Points>=10000:
    print("钻石会员")#print("")
elif 500<=consumption<1000 and 5000<=Points<10000:
    print("白金会员")
elif 200<=consumption<500 and 2000<=Points<5000:
    print("黄金会员")
elif 100<=consumption<200 and 1000<=Points<2000:
    print("白银会员")
elif 50<=consumption<100 and 500<=Points<1000:
    print("青铜会员")
elif consumption<50 and 0<=Points<500:
    print("普通会员")
else:
    print("未知会员")