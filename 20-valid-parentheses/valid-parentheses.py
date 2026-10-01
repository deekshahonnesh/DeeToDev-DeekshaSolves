class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map={")":"(", "}":"{", "]":"["}
        for char in s:
            if char in map.values():
                stack.append(char)
            elif char in map.keys():
                if stack == [] or map[char] != stack.pop():
                    return False
        return True if stack == [] else False
        