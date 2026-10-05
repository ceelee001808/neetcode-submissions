class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0 

        for n in nums:
            #check if its the start of a sequence 
            if (n-1) not in numSet:
                length = 0 
                while (n + length) in numSet: #check current number
                    length += 1

                longest = max(length, longest) #update longest

        return longest




    

