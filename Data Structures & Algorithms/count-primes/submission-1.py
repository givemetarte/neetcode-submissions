class Solution:
    def countPrimes(self, n: int) -> int:
        """
        n = 18 
        sqrt(18) = 4.2xxx 
        약수: 2,3,6,9 > 제곱근보다 낮은 곳까지 확인하면 됨 
        """
        def is_prime(num):
            for i in range(2,int(num**0.5)+1):
                if num % i == 0:
                    return False
            return True 

        cnt = 0 
        for num in range(2, n): 
            if is_prime(num) == True: 
                cnt += 1
        
        return cnt



