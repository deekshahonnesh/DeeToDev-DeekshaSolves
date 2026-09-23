class Solution:
    def minOperations(self, nums: list[int], x: int,i=0,j=None,u=0) -> int:
        
        #if j is None:
    
        #    j = len(nums) - 1
    
        #

    #
       
        #if x == 0:
    
        #   return u  
    
        #
    
        #if x < 0 or i > j:
    
        #    return float('inf') 
#
   
    #
       
        #t = x - nums[i]
    
        #p = x - nums[j]
#
   
    #
       
        #take_left =self. minOperations(nums, t, i + 1, j, u + 1)
#
       
        #take_right = self.minOperations(nums, p, i, j - 1, u + 1)
#
   
    #
       
        #if min(take_left,take_right)==None:
    
        #    return -1
    
        #return min(take_left,take_right)
#
        total_sum = sum(nums)
        target = total_sum - x
        
        # If the total sum equals x, we must remove all elements
        if target == 0:
            return len(nums)
        # If x is larger than the entire array sum, it's completely impossible
        if target < 0:
            return -1
            
        max_len = -1
        current_sum = 0
        left = 0
        
        # Sliding window strategy to find the longest middle subarray
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink the window if the sum exceeds our target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                
            # If we hit the exact target, track the longest window size
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
                
        # If max_len was updated, return remaining elements; otherwise return -1
        return len(nums) - max_len if max_len != -1 else -1
