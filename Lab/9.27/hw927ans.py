import random
import math


def timer(func):
    def func_wrapper(*args, **kwargs):
        from time import time
        time_start = time()
        result = func(*args, **kwargs)
        time_end = time()
        time_spend = time_end - time_start
        print('\n{0} cost time {1} s\n'.format(func.__name__, time_spend))
        return result
    return func_wrapper


def select_odd():
    sum = 1
    for i in range(1, 100):
        if i % 2:
            sum *= i
            print(i, end="\t")
    print(sum)


def reverse_list1(lst):
    return lst[::-1]


def reverse_list2(lst):
    return lst.reverse()


def reverse_list3(lst):
    return list(reversed(lst))


def dup_string(s):
    i = 1
    cur = 1
    res = 1
    while i < len(s):
        if s[i] == s[i-1]:
            i += 1
            cur += 1
        else:
            i += 1
            cur = 1
        if cur > res:
            res = cur
    return res


def replace_string(s):
    return s.replace(" ", '')


@timer
def mc():
    S = (1.0 - 0.0) * 2
    N = 100000
    C = 0
    for i in range(N):
        x = random.uniform(0.0, 1.0)
        y = random.uniform(0.0, 2.0)
        if y <= x ** 2 + x ** 3:
            C += 1
    I = C * S / N
    return I


@timer
def square_root_1():
    c = 2
    i = 0
    g = 0
    for j in range(0, c+1):
        if j * j > c and g == 0:
            g = j - 1
    while (abs(g * g - c) > 0.0001):
        g += 0.0001
        i += 1

    return g


@timer
def square_root_2():
    i = 0
    c = 2
    m_max = c
    m_min = 0
    g = (m_min + m_max)/2
    while (abs(g*g - c) > 0.00001):
        if (g * g < c):
            m_min = g
        else:
            m_max = g
        g = (m_min + m_max) / 2
        i += 1
    return g


@timer
def square_root_3():
    c = 2
    g = c/2
    i = 0
    while (abs(g*g - c) > 0.00001):
        g = (g + c/g)/2
        i = i + 1
    return g


@timer
def calc_pi_1():
    times = 1000000
    count = 0
    counter = 0
    pi = 0
    while True:
        if counter >> 25:
            break
        for i in range(times):
            x = random.random()
            y = random.random()
            if x*x + y*y < 1:
                count += 1
            counter += 1

        pi = 4 * count/counter
    return pi

@timer
def calc_pi_2():
    n = 6
    res = 1
    for i in range(14):
        n = 2 * n
        res = math.sqrt(2-2*math.sqrt(1-(res/2)**2))
        # print(n,n*res/2)
    return n*res/2

@timer
def calc_pi_3():
    n = 10
    t = n+10  # ?????????10?????????????????????????????????
    b = 10**t  # ?????????????????????t??????????????????10^t
    x1 = b*4//5  # ????????????4/5?????????
    x2 = b // -239  # ????????????1/239?????????
    s = x1+x2  # ???????????????
    n *= 2  # ??????????????????????????????????????????n???
    for i in range(3, n, 2):  # ????????????=3?????????n,??????=2
        x1 //= -25  # ??????????????????1/5???????????????
        x2 //= -57121  # ??????????????????1/239???????????????
        x = (x1+x2) // i  # ?????????????????????????????????????????????
        s += x  # ?????????
    pai = s*4  # ????????
    pai //= 10**10  # ???????????????
    return pai / 10**10


@timer
def calc_pi_4():
    s = 0
    result = 0
    for i in range(0, 10000):
        s += (-1)**i / (2*i+1)
        result = s*4
    return result

if __name__ == "__main__":
    
    # print(calc_pi_3())
    # print(calc_pi_4())
    # print(square_root_3())
    # print(square_root_2())
    # print(square_root_1())
    # print(mc())
    # print(replace_string("Data Scienct and Engineering"))
    # print(dup_string("abbbdcc"))
    # print(reverse_list1([1, 2, 3, 4, 5]))
    print("end")