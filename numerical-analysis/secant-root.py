def newton_root(x0, x1, eps):
    cnt = 0
    while True:
        f0 = 1 * x0 ** 3 - 3 * x0 - 1
        f1 = 1 * x1 ** 3 - 3 * x1 - 1
        x_next = x1 - (x1 - x0) / (f1 - f0) * f1
        print(x0, x1, cnt)

        if abs(x1 - x_next) < eps:
            print(x1, x_next)
            break
        
        x0 = x1
        x1 = x_next
        cnt += 1
             

if __name__ == '__main__':
    x0, x1 = 2, 1.9
    eps = 0.0001
    newton_root(x0, x1, eps)
