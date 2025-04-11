size=int(input("请输入棋盘的大小:"))
for i in range(1,size+1):#外层循环，用于控制棋盘的行数
    for j in range(1,size+1):#内层循环，用于控制一行中每个位置的制表符
        if i==1 and j==1:#左上角位置，输出制表符
            print("┌",end='')
        elif i==1 and j==size:#右上角位置，输出制表符-
            print("┐",end='')
        elif i==size and j==1:#左下角位置，输出制表符L
            print("└",end='')
        elif i== size and j== size: #右下角位置，输出制表符
            print("┘",end='')
        elif j==1:#左侧一列，输出制表符上
            print("├",end='')
        elif i== size:#底部一行，输出制表符上
            print("┴",end='')
        elif j== size: #右侧一列，输出制表符-
            print("┤",end='')
        elif i== 1:#顶部一行，输出制表符┮
            print("┬",end='')
        else:#其他位置
            print("┼",end='')
    print('')