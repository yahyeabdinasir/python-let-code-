from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        # check every pair of numbers
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]





if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([10, 20, 20], 30))  # [0, 1]
    print(s.twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print(s.twoSum([3, 2, 4], 7))  # [1, 2]
    print(s.twoSum([3, 3], 6))  # [0, 1]
