class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []                      # collects every valid triplet we find

        nums.sort()                   # sort so equal values sit next to each other
                                      # and we can move pointers based on sum size
                                      # e.g. [-1,0,1,2,-1,-4] -> [-4,-1,-1,0,1,2]

        for i, a in enumerate(nums):  # i = index, a = value; 'a' is fixed as the FIRST number of the triplet
            if i > 0 and a == nums[i - 1]:   # same value as the previous 'a'?
                continue                     # skip it, or we'd find the same triplets again

            l, r = i + 1, len(nums) - 1  # l starts just right of 'a', r starts at the far end
                                         # we search the section to the right of 'a' for two numbers
                                         # that add up to -a

            while l < r:                 # keep going until the pointers meet
                threeSum = a + nums[l] + nums[r]   # total of the current three numbers

                if threeSum > 0:         # too big: we need a smaller number
                    r -= 1               # move r left, since values shrink going left

                elif threeSum < 0:       # too small: we need a bigger number
                    l += 1               # move l right, since values grow going right

                else:                    # exactly 0, so we found a triplet
                    res.append([a, nums[l], nums[r]])  # save it

                    l += 1               # move l forward to look for a different pair

                    while l < r and nums[l] == nums[l - 1]:  # new nums[l] same as the one we just used?
                        l += 1                               # keep skipping, to avoid a duplicate triplet
                                         # r doesn't need to move here: once nums[l] changes,
                                         # the sum is no longer 0, and the checks above fix r

        return res                       # every unique triplet that sums to 0