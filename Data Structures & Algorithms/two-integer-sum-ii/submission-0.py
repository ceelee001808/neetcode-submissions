class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointers
        l,r = 0, len(numbers)-1 #left pointer at 0 and right pointer at last index (length of numbers minus 1)
        while l<r:
            curSum = numbers[l] + numbers[r]
            if curSum > target: #if current sum greater than target, take right pointer and shift to the left
                r -= 1
            elif curSum < target:
                l +=1 #vice-versa shift left pointer to right
            else: #if current sum exactly equal to target, return indices exaclty equal to l,r (but based on 1 so add one to each)
                return [l+1, r+1]
        return 



