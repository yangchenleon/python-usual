import numpy as np

def SOR(a, b, w, x, eps):
    l = np.tril(a, -1)
    u = np.triu(a, 1)
    d = np.diag(np.diag(a))
    # print(u)
    
    bw = np.matmul(np.linalg.inv(d + w * l), (1 - w) * d - w * u)
    fw = w * np.matmul(np.linalg.inv(d + w * l), b)
    # print(bw, fw)

    cnt = 0
    while (True):
        p = 0
        tmp = x
        x = np.matmul(bw, x.T) + fw
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
    a = np.array([[3, 2, 1], [-5, 7, 3], [2, -5, 7]])
    b = np.array([-5, 13, 3])
    x = np.array([1, 1, 1])
    w = 0.9
    eps = 0.000001
    SOR(a, b, w, x, eps)
    
 