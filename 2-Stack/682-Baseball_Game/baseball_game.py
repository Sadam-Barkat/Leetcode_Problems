class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for val in operations:
            stack.append(val)
            if stack[-1] == "C":
                stack.pop()
                stack.pop()
            elif stack[-1] == "D":
                stack.pop()
                stack.append(int(stack[-1]) * 2)
            elif stack[-1] == '+':
                stack.pop()
                stack.append(int(stack[-1]) + int(stack[-2]))
                  
        stack = [int(x) for x in stack]
        return sum(stack)      
        