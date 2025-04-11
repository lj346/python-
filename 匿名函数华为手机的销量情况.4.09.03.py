phone=[('华为 P60',4887.0,210),('华为Mate 40E Pro',4699.0,90),('华为 nova 10 青春版',1698.0,102),
       ('华为 P50 Pro',3897.0,88),('华为畅享',999.0,152)]
sorted_phone = sorted(phone, key=lambda phone: phone[2], reverse=True)
for name, price, sales in sorted_phone:
       print(f"{name}\t,{price}\t,{sales}")