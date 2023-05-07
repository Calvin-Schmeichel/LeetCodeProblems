class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for k in range(0, len(nums)):
            for n in range(k+1, len(nums)):
                if nums[n] + nums[k] == target:
                    return([k,n])
                    exit()

print(Solution.twoSum(Solution, [2,7,11,15], 9))