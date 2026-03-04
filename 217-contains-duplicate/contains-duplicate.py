class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        window = set()
        i = 0
        for i in range (len(nums)):
            if len(nums) != len(set(nums)):
                return True
            else:
                return False


        