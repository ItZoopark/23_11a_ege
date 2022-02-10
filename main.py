# Задачи из Решу ЕГЭ --------------------
def f(x, y):
    if x == y:
        return 1
    elif x > y:
        return 0
    elif x < y:
        return f(x + 1, y) + f(x + 2, y) + f(x * 2, y)


# print(f(3, 10)*f(10, 12))

def f_15117(x, y):
    if x == y:
        return 1
    elif x > y or x == 15:
        return 0
    elif x < y:
        return f_15117(x + 1, y) + f_15117(x + 2, y)


# print(f_15117(3, 9) * f_15117(9, 20))


def f_5849(x, y):
    if x == y:
        return 1
    elif x > y:
        return 0
    elif x < y:
        return f_5849(x + 1, y) + f_5849(10 + x, y)


# print(f_5849(35, 57))

def f_3303(x, n, res):
    if n == 10:
        res.add(x)
    else:
        f_3303(x + 2, n + 1, res)
        f_3303(x + 3, n + 1, res)


res = set()
f_3303(2, 0, res)


# print(len(res))


# Задачи из Полякова -----------------------------

def fibo(n):
    p1 = 0
    p2 = 1
    next = 1
    for _ in range(n - 2):
        p1 = p2
        p2 = next
        next = p1 + p2
    return next


def fibo_more(x):
    p1 = 1
    p2 = 1
    next = 2
    while next <= x:
        p1 = p2
        p2 = next
        next = p1 + p2
    return next

print(fibo_more(13))

def f_4852(x, y):
    if x == y:
        return 1
    elif x > y:
        return 0
    else:
        return f_4852(x + 1, y) + f_4852(x + 3, y) + f_4852(fibo(x), y)


# print(f_4852(6, 21))
