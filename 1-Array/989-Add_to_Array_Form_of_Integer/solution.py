class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        import sys
        sys.set_int_max_str_digits(100000)
        
        number = int(''.join(map(str, num)))
        number = number + k
        arr = [int(digit) for digit in str(number)]

        return arr