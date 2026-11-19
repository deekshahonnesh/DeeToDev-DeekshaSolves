class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        stack = []
        seen = set()

        for idx, char in enumerate(s):
            if char not in seen:  # <--- Must wrap ALL lines below it!
               while stack and char < stack[-1] and idx < last_occurrence[stack[-1]]:
                    seen.remove(stack.pop())
            
               seen.add(char)
               stack.append(char)

        return "".join(stack)
