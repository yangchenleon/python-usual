import math

a, b = 0, math.pi # 区间端点
I = -12.0703463164 # 精确解

F_a = math.e ** a * math.cos(a)
F_b = math.e ** math.pi * math.cos(b)
ls = [-1] # 存放E_n

for i in range(1,9):
    n = 2 ** i
    h = (b-a) / n

    p = q = 0
    # 计算复化求积公式中的和式
    for j in range(1, 2*n, 2):
        p += math.e ** (j*b/(2*n)) * math.cos(j*b/(2*n))
    for k in range(2, 2*n, 2):
        q += math.e ** (k*b/(2*n)) * math.cos(k*b/(2*n))

    S_n = h / 6 * (F_a + 4*p + 2*q + F_b)
    E_n = I - S_n

    ls.append(str(E_n))
    print('Sn={:.10f}  En={:.2E}  En/E2n={:.2f}'.format(S_n, E_n, float(ls[i-1])/float(ls[i])), '\t','n={}'.format(n))
