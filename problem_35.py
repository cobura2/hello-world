#The number, 197, is called a circular prime because all rotations 
#of the digits: 197, 971, and 719, are themselves prime.
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#How many circular primes are there below one million?
from math import sqrt
from bisect import bisect_left
  
def is_prime(n, li):
    if n <= 3: 
        return True
    
    last_num = int(sqrt(n)+1) 
    for i in li:
        if i > last_num:
            break
        if (n % i == 0):
            return False
    return True
            
def prime_numbers(n):
    li = [2]
    for i in range(3, n):
        if is_prime(i, li) == True:
            li.append(i)
    return li

def is_in_prime_list(n):
    global prime_list
    i = bisect_left(prime_list, n)
    return( i != len(prime_list) and prime_list[i] == n )

def GenRotations(num):
    li = []
    num_digits = len(str(num))
    mult = 10**(num_digits-1)
    for i in range(1, num_digits+1): 
        li.append(num)
        msd = num / 10
        lsd = num % 10
        num = lsd * mult + msd
    return li

def check_num(i):
    li = GenRotations(i)
    for i in li:
        if (is_in_prime_list(i) == False):
            return False
    return True
        
prime_list = prime_numbers(1000000)
count = 0
for i in prime_list:
    if check_num(i) == True:
        count += 1
        print i, count
