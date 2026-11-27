class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
    
    # A repeating pattern can't be longer than half the string
        for n in range(1, (length // 2) + 1):
        
        # Only check lengths that divide evenly into the total length
            if length % n == 0:
               pattern = s[:n]
            
            # Multiply the pattern to see if it matches the original string
               if pattern * (length // n) == s:
                   return True
                
        return False


