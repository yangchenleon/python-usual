import math

def step_scan(fn, x_range, step):
    l, r = x_range
    bgest_root_range = []
    for x in range(l, r + 1, step):
        val_l = fn(x)
        val_r = fn(x+1)
        if val_r * val_l <= 0:
            print(x, x + 1)
            bgest_root_range = [x, x + 1]
    return bgest_root_range

def bisection_root(fn, x_range, eps):
    cnt = 0
    xl, xr = x_range
    xs = [xl, (xl + xr) / 2, xr]
    while True:
        vals = [0, 0, 0] # l, m, r
        for i, x in enumerate(xs):
            vals[i] = fn(x)
        print(xs, vals[1])
        if abs(vals[1]) < eps:
            print(cnt, xs[1], vals[1])
            break

        if vals[0] * vals[1] >= 0:
            xs[0] = xs[1]
        else:
            xs[2] = xs[1]
        xs[1] = (xs[0] + xs[2]) / 2
        cnt += 1
        

if __name__ == '__main__':
    cofs = [0, 3, -4.8, -0.51]
    # fn = lambda x: cofs[0] * x**3 + cofs[1] * x**2 + cofs[2] * x + cofs[3]
    fn = lambda x: 3 * x ** 2 - math.exp(x)
    step = 1
    x_range = [-100, 100]
    step_scan(fn, x_range, step)

    x_range = [1.5, 1.8]
    eps = 0.00001
    bisection_root(fn, x_range, eps)

