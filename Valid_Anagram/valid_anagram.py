class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        for element in t:
            if element not in s:
                return False
            if t.count(element)!=s.count(element):
                return False
        return True
