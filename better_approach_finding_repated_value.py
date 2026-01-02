from typing import List
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        not_seen = []
        seen = []


        for n in range(len(nums)):
            if nums[n] not in not_seen:
                not_seen.append(nums[n])
            else:
                seen.append(nums[n])

        return seen[0]



if __name__ == "__main__":
    s = Solution()
    print(s.repeatedNTimes([10, 10, 20, 54]))


