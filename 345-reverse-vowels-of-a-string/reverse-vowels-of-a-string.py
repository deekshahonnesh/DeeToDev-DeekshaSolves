class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        vowels = "aeiouAEIOU"
    
    # Start 'i' at the beginning and 'j' at the end
        i = 0
        j = len(chars) - 1
    
        while i < j:
             if chars[i] not in vowels:
                i += 1  # Change 'i' number because it's not a vowel (j remains same)
             elif chars[j] not in vowels:
                j -= 1  # Change 'j' number because it's not a vowel (i remains same)
             else:
            # Both are vowels! Swap them and move both pointers
                 chars[i], chars[j] = chars[j], chars[i]
                 i += 1
                 j -= 1
            
        return "".join(chars)
        