class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence.lower()
        alphabats = "abcdefghijklmnopqrstuvwxyz"
        count = 0

        for i in alphabats:
            if i in sentence:
                count += 1
        if count == 26:
            return True
        else:
            return False          
