import math
import numpy as np 
from numpy import *  


def T_2n(a, b, n, T_n):       #计算T0(h/2)的函数, a 积分下限，b 积分上限, n是区间等分数
    if n<1:                
        print('n should larger than 1')
    h = (b - a)/n             #步长      
    sum_f = 0.            #初始化，中间变量
    for k in range(0, n):
        sum_f = sum_f + fun(a + (k + 0.5)*h)
    T_2n = T_n/2. + sum_f*h/2.
    return T_2n


def Romberg(a, b, err_min):
    kmax = 6
    tm = zeros(kmax,dtype = float)      # 第m行所有的元素
    tm1 = zeros(kmax,dtype = float)     #第m+1行所有的元素   
    tm[0] = 0.5*(b-a)*(fun(a) + fun(b))  # 初始值
    print(tm)
    err = 1.
    k = 0
    np.set_printoptions(precision = 9)
    while(err>err_min and k <kmax-1):  #控制循环次数
        n = 2**k                      # n是区间等分数
        m = 1
        tm1[0] = T_2n(a, b, n, tm[0]) 
        while(err>err_min and m <= (k+1)):  #控制循环次数
            tm1[m] = tm1[m-1]+(tm1[m-1]-(tm[m-1]))/(4.**m-1)
            result = tm1[m]
            err1 = abs(tm1[m]-tm[m-1])
            err2 = abs(tm1[m]-tm1[m-1])
            err = min(err1,err2)
            m = m+1
        tm = np.copy(tm1)
        k = k+1
        print(tm)     
    return result

def fun(x):           #被积函数,  x为自变量
    if x < 0:
        print('err')
        # return 99999
    else:
        # f =   math.log(x)
        f = math.exp(-x**2)
    return f
f1 = Romberg(0, 1,1e-5)  #主程序（分别输入上下限，误差）
print('result = ',f1)
