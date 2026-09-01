from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        for i in range(len(s2) - len(s1) + 1):
            substring = s2[i:i + len(s1)]

            if Counter(substring) == Counter(s1):
                return True

        return False