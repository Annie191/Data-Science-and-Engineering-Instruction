#递归求阶乘
def Jiecheng(a):
    if a <= 1:
        return 1
    else:
        return Jiecheng(a-1)*a

print(Jiecheng(3))            