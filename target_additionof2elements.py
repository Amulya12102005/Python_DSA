arr=[1,12,15,65,13,95,76]
target=25
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        sum = arr[i]+arr[j]
        if sum == target:
            print(arr[i],arr[j])






class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums-1)):
            for j in range (i+1,len(nums)):
                if target==nums[i]+nums[j]:
                    return{i,j}
        return{}


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Bubble sort in ascending order
        for i in range(len(nums)):
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:  # FIXED condition
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        # Check adjacent elements for duplicates
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False
