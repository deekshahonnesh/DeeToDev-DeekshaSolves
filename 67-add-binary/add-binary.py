class Solution:
    def addBinary(self, a: str, b: str) -> str:
    
    # 1. Reverse the strings to add from right to left easily
        m, n = list(a[::-1]), list(b[::-1])
    
    # 2. Pad the shorter list with "0"s until they are equal length
        while len(m) < len(n):
             m.append("0")
        while len(n) < len(m):
            n.append("0")
        
        result = []
        carry = 0
    
    # 3. Loop through and perform binary addition
        for i in range(len(m)):
           digit_a = int(m[i])
           digit_b = int(n[i])
        
        # Calculate sum of digits and current carry
           total = digit_a + digit_b + carry
           # Determine current bit and next carry
           result.append(str(total % 2))
           carry = total // 2
        
    # 4. If there is a leftover carry, add it to the end
        if carry:
           result.append(str(carry))
        
    # 5. Reverse back to get the final correct order
        return "".join(result[::-1])    