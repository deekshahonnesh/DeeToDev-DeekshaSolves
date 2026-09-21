class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
    
    
    
        dp = [0] * k

    
        for num in nums:
            current_remainder=num%k
            next_dp = [0] * k
        
        
            next_dp[current_remainder] += 1
        
        
            for prev_remainder in range(k):
                if dp[prev_remainder] > 0:
                    new_remainder = (prev_remainder * current_remainder) % k
                    next_dp[new_remainder] += dp[prev_remainder]
            for remainder in range(k):
                result[remainder] += next_dp[remainder]
            
        
            dp = next_dp
        
        return result

        
