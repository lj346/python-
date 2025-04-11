goods={'可口可乐':2.5,'百事可乐':2.5,'冰红茶':3,'脉动':3.5,
       '果缤纷':3,'绿茶':3,'茉莉花茶':3,'尖叫':2.5}
print("""
    --------------------
    可口可乐:2.5元
    百事可乐:2.5元
    冰红茶:3元
    脉动:3.5元
    果缤纷:3元
    绿茶:3元
    茉莉花茶:3元
    尖叫:2.5元
    --------------------
    """)

def user_input():
    cart = {}
    while True:
        drink = input("请输入您想要购买的饮品名称（输入q结算）：\n")
        if drink == 'q':
            break
        if drink not in goods:
            print("商品名称不正确，请重新输入。")
            continue
        num_input = int(input("请输入您想要购买的数量（请输入正整数）：\n"))
        if num_input<= 0:
            print("商品数量不合法，请重新输入。")
            continue
        # 累加购物车内的商品数量
        if drink in cart:
            cart[drink] += num_input
        else:
            cart[drink] = num_input
    print("\n您购买的商品如下：")
    num_a=0
    for name, num in cart.items():
        price = goods[name]
        sum= price * num
        num_a += sum
        print(f"{name} x {num} = {sum:.2f}元")
    print(f"共计{num_a}元")
user_input()
