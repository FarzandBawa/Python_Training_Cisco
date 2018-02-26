import time


def time_it(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("time taken by square:", (end - start) * 1000, "mil sec")
    return inner


@time_it
def square(num):
    # start = time.time()
    res = []
    for i in num:
        res.append(i * i)
    # end = time.time()
    # print("time taken by square:", (end - start) * 1000, "mil sec")


@time_it
def cube(num):
    # start = time.time()
    res = []
    for i in num:
        res.append(i**3)
    # end = time.time()
    # print("time taken by square:", (end - start) * 1000, "mil sec")


num = range(1, 100000)
square(num)
cube(num)
