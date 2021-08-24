
def fib(n):
    n_1 = 0
    n_2 = 1
    ar = []
    count =0
    if n <= 0:
        print('-ve number')
    elif n==1:
        return n_1
    else:
        while count<n:
            
            ar.append(n_1)
            nth = n_1 + n_2
            n_1 =n_2
            n_2 = nth
            count += 1
    return ar
    


print(fib(4))