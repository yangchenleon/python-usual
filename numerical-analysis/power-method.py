import numpy as np

def power_method(a, v, eps):
    times = 0
    u = v / v[np.argmax(np.abs(v))]
    lmd = 0
    print(v.T, u.T)

    while True:
        tmp_lmd = lmd
        v = np.matmul(a, u)
        lmd = v[np.argmax(np.abs(v))]
        u = v / lmd
        print(v.T, u.T, lmd)
        
        if np.abs(lmd - tmp_lmd) < eps:  # 精度满足要求，结束
            break
        times += 1
    
    print(times)
    print(lmd)
    print(u)
    # print(id(Lambda),id(tempL))

if __name__ == '__main__':
    # a = np.array([[-11, 11, 1], [11, 9, -2], [1, -2, 13]])
    a = np.array([[-26, 11, 1], [11, -6, -2], [1, -2, -2]])
    v = np.array([[1, 1, 1]]).T
    eps = 1e-3
    power_method(a, v, eps)
    # print(np.linalg.eigvals(a))