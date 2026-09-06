class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = [0.5]*len(nums)
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in store:
                return [store.index(difference), i]
            else:
                store[i] = nums[i]
             
