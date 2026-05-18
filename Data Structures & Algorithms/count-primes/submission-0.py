class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0

        primes = [2]
        
        for num in range(3, n+1):
            for div in primes: 
                if num % div == 0:
                    break 
            else: 
                primes.append(num)

        return len(primes)

"""
primes = [2]

num = 3 > div = 2 > 3 % 2 != 0 > primes = [2,3]
num=4 > div=2 > 4 % 2==0 > primes = [2,3]
num=5 > div=2 > 5%2 != 0 > pass 
      > div=3 > 5%3 != 0 > pass > primes = [2,3,5]
num=6 > div=2 > 6%2 == 0 > pass 
num=7 > div=2 > 7%2 != 0 > pass
      > div=3 > 7%3 != 0 > pass 
      > div=5 > 7%5 != 0 > pass > primes = [2,3,5,7]
...
"""