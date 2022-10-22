from multiprocessing import Pool

def f(x):
    for _ in range(20000000):
        x = x + 0.000001
    return x * x

if __name__ == '__main__':
    with Pool(16) as p:
        print(p.map(f, [1, 2, 3, 1, 2, 3]))
