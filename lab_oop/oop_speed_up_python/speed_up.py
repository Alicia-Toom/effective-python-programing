import profile
import functools 


print('Fingure out where time is spent with the profile modul')
print('-' * 79)

@functools.lru_cache(maxsize=None)
def fib(n):
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return fib(n - 1) + fib(n - 2)


def fib_seq(n): 
    seq = []
    if n > 0: 
        seq.extend(fib_seq(n - 1))
    seq.append(fib(n))
    return seq

profile.run('print(fib_seq(20)')