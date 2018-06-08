def iterativeFactorial(x):
    if(x==0): return 1
    factorial = 1
    for i in range(1,x+1):
        factorial*=i
    return factorial


def recursiveFactorial(x):
    if(x==0): return 1
    return x * recursiveFactorial(x-1)

print(iterativeFactorial(5))
print(recursiveFactorial(5))
