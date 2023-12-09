import numpy as np

def reverse_power_method(a, v, eps):
    times = 0
    u = v / v[np.argmax(np.abs(v))]
    lmd = 0
    print(v.T, u.T)

    while True:
        tmp_lmd = lmd
        v = np.matmul(np.linalg.inv(a), u)
        u = v / v[np.argmax(np.abs(v))]
        lmd = 1 / v[np.argmax(np.abs(v))]
        times += 1

        print(v.T, u.T, lmd)     
        if np.abs(lmd - tmp_lmd) < eps:  # 精度满足要求，结束
            break
        
    print(times)
    print(lmd)
    print(u)
    # print(id(Lambda),id(tempL))

if __name__ == '__main__':
    # a = np.array([[1, -1, 2], [-2, 0, 5], [6, -3, 6]])
    a = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
    v = np.array([[1, 1, 1]]).T
    eps = 1e-6
    reverse_power_method(a, v, eps)
    # print(np.linalg.eig(a))
