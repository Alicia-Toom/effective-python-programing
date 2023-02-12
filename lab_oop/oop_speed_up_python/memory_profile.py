import memory_profiler

log=open('memory_test.txt', 'w+')

@memory_profiler.profile(stream=log)
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

fib_seq(20)
log.close()
