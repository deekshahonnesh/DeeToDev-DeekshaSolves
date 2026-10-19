class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None:
           return True
        else:
            k="".join(char for char in s if char.isalnum())
            j=k.lower()
            if j==j[: : -1]:
                return True
            else:
                return False
        