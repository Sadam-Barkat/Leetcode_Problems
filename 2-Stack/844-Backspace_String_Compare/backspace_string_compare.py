class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(st: str) -> list:
            stack = []
            for char in st:
                if char == '#':
                    if stack:
                        stack.pop()  
                else:
                    stack.append(char)  
            return stack
        
        return process_string(s) == process_string(t)
