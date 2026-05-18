class Solution:
    def countPrimes(self, n: int) -> int:
        """
        에라토스테네스의 체 
        n = 14일 때 전체가 다 소수라 가정 
        {2,3,4,5,6,7,8,9,10,11,12,13}
        sqrt(14)==7 >> 7이하만 확인하면 됨 
        1) 2의 배수 삭제: {2,3,5,7,9,11,13}
        2) 3의 배수 삭제: {2,3,5,7,11,13}
        3) 4 없음 
        4) 5의 배수 삭제: {2,3,5,7,11,13}
        ....
        """
        primes = set(range(2,n))
        for num in range(2, int(n**0.5)+1):
            if num in primes: 
                primes -= set(range(num*2, n, num))
                # num*2부터 시작해서 n전까지 num만큼 더하면서 돔 
        return len(primes)

