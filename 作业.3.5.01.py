total_coal = 29.5# 总煤量
coal1_car=4# 第一辆汽车的载重量
coal1_car_num=3# 第一辆汽车运送煤的次数
remainder_coal=total_coal-(coal1_car_num*coal1_car)# 剩下的煤
coal2_car=2.5# 第二辆汽车的载重量
coal2_car_num=remainder_coal//coal2_car# 求第二辆汽车运送煤的次数（整数部分）
if remainder_coal % coal2_car!=0:
    coal2_car_num+=1
print("第二辆汽车运送次数：", coal2_car_num)