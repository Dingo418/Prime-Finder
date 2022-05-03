from typing import Literal


def isPrime(num):
    for i in range(2, num/2): #gets number and then sees if it is prime by using every single number and running modulus
        if num % i == 0:
            return False
    return True
def addtofile(data):
    open("primes.txt", "a").write(str(data)) #Just stores data at the end into a txt file

def primelist(end): #makes a list of prime numers from 2 to entered amount
    primes = []
    for n in range(2, end):
        if isPrime(n) == True:
            #print(n, "is prime")
            primes.append(n)
    addtofile(primes)

def isPrimev2(num, past_primes): #different compared to isprime() as it just using modulus on past known prime number, not complete number list
    for i in range(0, len(past_primes)):
        if num % past_primes[i] == 0:
            return False
    past_primes.append(num)
    return True

def primelist2(end): #speed up by 6 times
    primes = list()
    start = 2
    for n in range(start, end):
        if isPrimev2(n, primes) == True:
            #print(n, "is prime")
            primes.append(n) 
            addtofile("," + str(n)) #only did this to save if program dies

def contiune_primelist2():
    try:
        primes = list(map(int, open("primes.txt", "r").read().split(","))) #only works if you take , at the start of primes.txt
    except (ValueError):
        primelist2(100)
        primes = [2,3]   
    end = 9999999999
    primes.pop(0)
    start = primes[len(primes)-1]
    for n in range(start, end):
        if isPrimev2(n, primes) == True:
            #print(n, "is prime")
            primes.append(n)
            addtofile("," + str(n) ) #only did this to save if program dies

if __name__ == "__main__":
    contiune_primelist2()
