class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s: #iterate every character in s
            if c.isalnum(): # if alnum..include in newSTR
                newStr += c.lower() #convert to lowercase
        return newStr == newStr[::-1] #syntax for reversing a string

