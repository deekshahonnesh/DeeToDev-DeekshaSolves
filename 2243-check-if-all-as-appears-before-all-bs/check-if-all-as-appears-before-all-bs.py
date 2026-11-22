class Solution:
    def checkString(self, s: str) -> bool:
        k = s.find("b")
        if k == -1:
            return True
        return "a" not in s[k:]