class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
           return False
        if  n == 1:
            return True
        
    # Continuously divide by 4 if there's no remainder
        while n % 4 == 0:
            n //= 4
            if n==1:
                return True
        
    # If it scales all the way down to 1, it's a power of 4
        
            
        return False