class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check to see if the strings are equal
        if len(s) != len(t):
            return False
        #use sorted funtion to compare to see if anagram
        return sorted(s) == sorted(t)

        