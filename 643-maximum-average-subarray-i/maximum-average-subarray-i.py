class Solution(object):
    def findMaxAverage(self, nums, k) -> float:
        curr_sum = max_sum = sum(nums[:k])
        #To compute the sum of the first k:
        for i in range(len(nums) - k):
            curr_sum += nums[i + k] - nums[i]
            max_sum = max(max_sum, curr_sum)

        return max_sum /(k)
        