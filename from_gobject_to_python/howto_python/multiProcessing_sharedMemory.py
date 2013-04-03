from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]
def g(n,a):
    print n.value
    print a[:]
if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p = Process(target=g, args=(num, arr))
    p.start()

#    print num.value
#    print arr[:]
