class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1=sorted(list(s))
        str2=sorted(list(t))
        if str1 == str2:
            return True
        return False
s="racecar"
t="carrace"
p=Solution()
p.isAnagram(s,t)
