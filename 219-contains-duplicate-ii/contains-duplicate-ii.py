class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        i = 0
        for i in range (len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            # the len of window must be within the value of k
            if len(window) > k:
                window.remove(nums[i - k])
        return False        


            



        