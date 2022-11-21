import os
import time

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
    
    # brutal force
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

def problem4(n):
    '''
    Largest palindrome product
    https://projecteuler.net/problem=4

    for n=2, 
        aba = 100*a + 10*b + a = 101*a + 10*b
        abba = 1000*a + 100*b + 10*b + a = 1001*a + 110*b = 11*(91*a + 10*b)
    for n=3, 
        abcba = 10001*a + 1010*b + 100*c
        abccba = 100001*a + 10010*b + 1100*c = 11*(9091*a + 910*b + 100*c)
    for n=4,
        abcdcba = 1000001*a + 100010*b + 10100*c + 1000*d
        abcddcba = 10000001*a + 1000010*b + 100100*c + 11000*d = 11*(909091*a + 90910*b + 9100*c + 1000*d)
    
    assume the largest palindrome product always has 2N digits
    '''
    def _isPalindrome(s):
        return str(s)==str(s)[::-1]
    
    maxProduct = 0
    s1, s2 = 0, 0
    for n1 in range(10**(n-1), 10**n):
        if n1%11!=0:
            continue
        for n2 in range(10**(n-1), 10**n):
            product = int(n1*n2)
            if product <= maxProduct:
                continue
            if _isPalindrome(product):
                s1 = n1
                s2 = n2
                maxProduct = product
    # print(s1, s2, maxProduct)
    return maxProduct

def problem5(n):
    '''
    Smallest multiple
    https://projecteuler.net/problem=5
    '''
    def _isPrime(s):
        if s==1:
            return False
        for j in range(2,s):
            if j*j>s:
                break
            if s%j==0:
                return False
        return True

    primeToExp = {}
    for i in range(1, n+1):
        if _isPrime(i):
            primeToExp[i] = 1
            continue
        for prime, exp in primeToExp.items():
            exp1 = 0
            while i%prime == 0:
                i = i//prime
                exp1 += 1
            primeToExp[prime] = max(exp, exp1)
    
    res = 1
    for prime, exp in primeToExp.items():
        res = res * prime**exp
    return res

def problem6(n):
    '''
    Sum square difference
    https://projecteuler.net/problem=6
    \sum_i i**3 = (\sum_i i)**2
    '''
    # can use formula directly
    
    res = 0
    for i in range(1,n+1):
        res += i**2 * (i-1)
    return res

def problem7(n):
    '''
    10001st prime
    https://projecteuler.net/problem=7
    '''
    primes = [2]
    number = 3
    while len(primes)<n:
        isPrime = True
        for prime in primes:
            if number%prime==0:
                isPrime = False
                break
        if isPrime:
            primes.append(number)
        number+=1
    return primes[-1]

def problem8(l):
    '''
    Largest product in a series
    https://projecteuler.net/problem=8
    '''
    num =  '73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'
    listSequences = num.split('0')
    listProducts = []
    
    def _findMaxProduct(sequence, l):
        if len(sequence)<l:
            return 0
        elif len(sequence)==l:
            product = 1
            for s in sequence:
                product = product * int(s)
            return product
        else:
            product = _findMaxProduct(sequence[:l], l)
            products = [product]
            for i in range(len(sequence)-l):
                product /= int(sequence[i])
                product *= int(sequence[i+l])
                products.append(product)
            return int(max(products))
            
    for sequence in listSequences:
        listProducts.append(_findMaxProduct(sequence, l))
    return max(listProducts)

def problem9():
    '''
    Special Pythagorean triplet
    https://projecteuler.net/problem=9
    a^2 + b^2 = c^2
    a + b + c = 1000
    a^2 + b^2 = (1000 - a - b)^2
    (1000 - a)*(1000 - b) = 2^5 * 5^6 = 625 * 800
    '''
    return (1000-625) * (1000-800) * (625+800-1000)

def problem10(n):
    '''
    Summation of primes
    https://projecteuler.net/problem=10
    '''
    sieve = [True]*(n)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, n):
        if i*i>n:
            break
        if sieve[i]:
            for j in range(i*2,n,i):
                sieve[j] = False
    res = 0
    for i, flag in enumerate(sieve):
        if flag:
            res += i
    return res



if __name__ == "__main__":
    print('problem1:\n', problem1(1000))
    print('problem2:\n', problem2(4000000))
    print('problem3:\n', problem3(600851475143))
    print('problem4:\n', problem4(3))
    print('problem5:\n', problem5(20))
    print('problem6:\n', problem6(100))
    # print('problem7:\n', problem7(10001))
    print('problem8:\n', problem8(13))
    print('problem9:\n', problem9())
    print('problem10:\n', problem10(2000000))