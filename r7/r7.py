class Averager():
    def __init__(self):
        self.series = []  #zmienna swobodna
    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)


avg = Averager()
print(avg(10))
print(avg(11))
print(avg(12))


def make_averager():
    series=[]
    # domkniecie
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        xx = 10
        return total / len(series)
    return averager

avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))

print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
print(avg.__closure__)
print(avg.__closure__[0].cell_contents) # wartosci w komorkach zmiennej swobodnej

print('make_averager2')
def make_averager2():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager

avg2 = make_averager2()
print(avg2(10))
print(avg2(11))
print(avg2(12))


import time

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)

# print('*' * 40, 'Calling snooze')
aa = snooze(.123)

factorial(6)

