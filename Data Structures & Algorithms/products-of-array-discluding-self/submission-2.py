class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


#reuse the result array and build the answer in two simple passes:
    #In the first pass, we fill res[i] with the product of all elements to the left of i (prefix product).
    #In the second pass, we multiply each res[i] with the product of all elements to the right of i (postfix product).
        