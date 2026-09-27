class Solution:
    import re
    def reverseParentheses(self, s: str) -> str:
        h=re.search(r"\(([^()]*)\)", s)

        while h: 
            s = re.sub(r"\(([^()]*)\)", lambda match: match.group(1)[::-1], s)
            h=re.search(r"\(([^()]*)\)", s)

        return s
        