class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:
           return False

    # 1. Pick the length of the FIRST number (1 digit, 2 digits, etc.)
        for i in range(1, n // 2 + 1):
        
        # 2. Pick where the SECOND number ends (1 digit, 2 digits, 3 digits, etc.)
            for j in range(i + 1, n):
                first = num[:i]
                second = num[i:j]

            # 3. Skip invalid numbers with leading zeros (like "01" or "05")
                if (len(first) > 1 and first[0] == '0') or (len(second) > 1 and second[0]     ==     '0'):
                   continue

            # 4. Convert strings to integers so we can do math, and set our starting pointer
                num1 = int(first)
                num2 = int(second)
                pos = j

            # 5. Keep adding and sliding forward until we finish the string
                while pos < n:
                     expected_sum = str(num1 + num2)
                
                # Check if the next characters in the string match our sum
                     if num[pos : pos + len(expected_sum)] == expected_sum:
                    # Shift numbers forward for the next addition
                       num1 = num2
                       num2 = int(expected_sum)
                       pos += len(expected_sum)
                     else:
                    # Mismatch! Stop this attempt and try the next 'j'
                        break

            # 6. If 'pos' reached the exact end of the string, we found a valid sequence!
                if pos == n:
                   return True

    # 7. Tried every possible combination and none reached the end
        return False

        