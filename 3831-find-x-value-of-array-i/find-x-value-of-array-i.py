class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
    
    
    
        dp = [0] * k

    
        for num in nums:
            current_remainder = num % k
        # next_dp calculates the updated counts for subarrays ending at this element
            next_dp = [0] * k
        
        # Choice 1: Start a brand-new single-element subarray at this number
            next_dp[current_remainder] += 1
        
        # Choice 2: Extend all existing past subarrays by multiplying them 
        # by our current element's remainder
            for prev_remainder in range(k):
                if dp[prev_remainder] > 0:
                    new_remainder = (prev_remainder * current_remainder) % k
                    next_dp[new_remainder] += dp[prev_remainder]
            for remainder in range(k):
                result[remainder] += next_dp[remainder]
            
        # Move the sliding window forward to process the next element
            dp = next_dp
        
        return result

        
