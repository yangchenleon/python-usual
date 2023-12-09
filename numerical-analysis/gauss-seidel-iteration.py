import numpy as np

def gauss_seidel(a, b, x, eps):
    l = np.tril(a, -1)
    u = np.triu(a, 1)
    d = np.diag(np.diag(a))
    # print(u)
    
    bs = np.matmul(-np.linalg.inv(d + l), u)
    fs = np.matmul(np.linalg.inv(d + l), b)
    # print(fs)

    cnt = 0
    while (True):
        p = 0
        tmp = x
        x = np.matmul(bs, x.T) + fs
        print(x)
        for i in range(len(x)):
            if np.abs(tmp[i] - x[i]) > p:
                p = np.abs(tmp[i] - x[i])
        cnt += 1
        if (p < eps):
            print(cnt)
            break
    print(x)

if __name__ == '__main__':
    a = np.array([[2, 1, 0], [1, 2, 1], [0, 1, 2]])
    b = np.array([3, -5, 4])
    eps = 0.001
    x = np.array([0, 0, 0])
    gauss_seidel(a, b, x, eps)
    
 