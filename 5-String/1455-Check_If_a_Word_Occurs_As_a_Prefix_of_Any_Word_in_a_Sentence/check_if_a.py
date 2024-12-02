class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        str_list = sentence.split()
        for i, char in enumerate(str_list):
            if char.startswith(searchWord):
                return i + 1  
        return -1
