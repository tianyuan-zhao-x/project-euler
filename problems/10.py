import os

def problem1(n):
    '''
    Multiple of 3 or 5
    https://projecteuler.net/problem=1
    '''
    # clever
    def _sumMultiplesBelow(n, multiple):
        return sum([multiple * (i+1) for i in range(n // multiple)])
    
    sumMultiple_3 = _sumMultiplesBelow(n-1, 3)
    sumMultiple_5 = _sumMultiplesBelow(n-1, 5)
    sumMultiple_15 = _sumMultiplesBelow(n-1, 15)
    s1 = sumMultiple_3 + sumMultiple_5 - sumMultiple_15
    
    # brute force
    s2 = 0
    for i in range(1,n):
        if (i%3==0) or (i%5==0):
            s2 += i
    return s1, s2

def problem2(n):
    '''
    Even Fibonacci numbers
    https://projecteuler.net/problem=2
    '''
    s1, s2 = 1, 2
    res = 0
    while s2 <= n:
        if s2%2==0:
            res += s2
        s1, s2 = s2, s1+s2
    return res

def problem3(n, smallestPriceFactor=2):
    '''
    Largest prime factor
    https://projecteuler.net/problem=3
    '''
    # print(n, smallestPriceFactor)
    def _isPrime(s):
        for j in range(2,s):
            if j*j>s:
                break
            if s%j==0:
                return False
        return True
    
    if _isPrime(n):
        return n
    
    for i in range(smallestPriceFactor,n):
        if n%i!=0:
            continue
        while n%i==0:
            n = n//i
        if n==1:
            return i
        else:
            return problem3(n, i)

def problem4(digits):
    '''
    Largest palindrome product
    https://projecteuler.net/problem=4
    '''
    
    
    

if __name__ == "__main__":
    print('problem1:\n', problem1(1000))
    print('problem2:\n', problem2(4000000))
    print('problem3:\n', problem3(600851475143))
    print('problem4:\n', problem4(3))
    # print('problem5:\n', problem5(4000000))
    # print('problem6:\n', problem6(4000000))
    # print('problem7:\n', problem7(4000000))
    # print('problem8:\n', problem8(4000000))
    # print('problem9:\n', problem9(4000000))
    # print('problem10:\n', problem10(4000000))