from typing import List


class Solution:
    def sum_of_even(self, nums: List[int]) -> int:

        greatest = 0



        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] > greatest:
                    greatest = nums[j] **2

            return greatest





if __name__ == "__main__":
    s = Solution()
    print(s.sum_of_even([1, 2, 10]))
