class Solution:
    def simplifyPath(self, path: str) -> str:
        # 1. Split the path by "/"
    # Example: "/a/./b/../../c/" becomes ["", "a", ".", "b", "..", "..", "c", ""]
         components = path.split("/")
         stack = []
    
         for portion in components:
        # 2. Ignore empty strings (from multiple slashes like `//`) and single dots `.`
             if portion == "" or portion == ".":
                continue
        
        # 3. If it's `..`, go up one level by popping from the stack (if stack isn't empty)
             elif portion == "..":
                 if stack:
                    stack.pop()
        
        # 4. Any other text (like "a", "...", "chr") is a valid directory name
             else:
                stack.append(portion)
            
    # 5. Join the directories back together with a single leading slash
         return "/" + "/".join(stack)
        