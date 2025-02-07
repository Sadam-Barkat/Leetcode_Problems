class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []  
        j = 0
        s1 = [i for i in s]

        for i in range(len(s1) -1):
            if s1[i] == '(':
                stack.append(s1[i])
            if stack and s1[i+1] == ')':
                stack.pop()
                j += 2
        return (len(s1) - j)

