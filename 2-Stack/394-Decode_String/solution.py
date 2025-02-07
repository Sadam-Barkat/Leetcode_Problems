class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        string_stack = []
        k = 0    

        for c in s:
            if c.isdigit():
                k = (k * 10) + int(c)
            
            elif c == '[':
                string_stack.append(c)
                num_stack.append(k)
                k = 0
            elif c == ']':
                temp = []
                while string_stack and string_stack[-1] != '[':
                    temp.insert(0, string_stack.pop())
                string_stack.pop()
                count = num_stack.pop()

                replacement = "".join(temp) * count
                string_stack.append(replacement)
            else:
                string_stack.append(c)    

        return "".join(string_stack)        