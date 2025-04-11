def func(number):
    if number==2:
        return 1
    else:
        return number*func(number-1)
user_input=func(20)
print(user_input)