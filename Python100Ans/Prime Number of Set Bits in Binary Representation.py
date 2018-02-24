class Solution:
    def countPrimeSetBits(self, L, R):
        primes = {2,3,5,7,11,13,17,19,23,29}
        ans = 0
        for i in range(L,R +1):
            b = bin(i)
            c= 0
            for j in b:
                if j == '1':
                    c+=1
            if c in primes:
                ans += 1
        return ans