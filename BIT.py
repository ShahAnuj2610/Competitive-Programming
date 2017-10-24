def update(x, delta):
    while x <= n:
        BIT[x] += delta
        x += x&-x

def query(x):
    summ = 0
    while x > 0:
        summ += BIT[x]
        x -= x&-x
    return summ
