class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        number = int(''.join(map(str, digits)))
        number = number + 1
        digits = [int (digits) for digits in str(number)]

        return digits