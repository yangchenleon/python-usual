import math

def quadratic_interpolation(xs, fs, x):
    result = 0
    for i, y in zip(xs, fs):
        item = 1
        for j in xs:
            if j == i:
                continue
            item *= (x - j) / (i - j)
        item *= y
        result += item
    return result

if __name__ == '__main__':
    fn = lambda x: math.e ** (-x ** 2)
    # xs = [0.6, 0.2, 0.4, 0]
    # fs = [0.697676, 0.960789, 0.852114, 1]
    fs = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
    xs = [0, 0.19956, 0.39646, 0.58813, 0.77210, 0.94608]
    x = 0.45
    print(fn(x), quadratic_interpolation(xs, fs, x))


