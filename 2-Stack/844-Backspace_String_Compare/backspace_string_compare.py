<<<<<<< HEAD
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
=======
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
>>>>>>> b89779cf6f400de0112ab3ee025a93cf9be9b717
