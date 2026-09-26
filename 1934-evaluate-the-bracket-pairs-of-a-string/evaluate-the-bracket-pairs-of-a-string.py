class Solution:
    import re
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        k=dict(knowledge)
        #while is used mainly to repeat things until it is wrong
#for is used to match the things and assinging until it ends
        while True:
            h=re.search(r"\((.*?)\)",s)
            if h:
                extract=h.group(1)
            else:
                break
        
            #to return question mark we should use string
#we should use the .get mainly used in dict and works as if and else
            rs=k.get(extract,"?")
            s=s.replace(f"({extract})",rs)
            
        return s
        