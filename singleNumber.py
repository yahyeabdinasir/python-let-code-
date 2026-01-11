from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:


        # this is the best way that we can solve that king of the question
        for num in nums:
            if nums.count(num)==1:
                return  num


        # and also this question we have used the external library to solve the problem
        # counting = Counter(nums)
        # for num , count  in counting.items():
        #     if count == 1:
        #         return  num
        #






        # so the below answer it can also possible but it taks some memory it be 0(0)

        # non_duplicate = []
        # duplicate = []
        #
        # for i in nums:
        #     if i not in non_duplicate:
        #         non_duplicate.append(i)
        #     else:
        #         duplicate.append(i)
        # print(non_duplicate)
        # print(duplicate)
        #
        #
        # for j in non_duplicate:
        #     if j not in duplicate:
        #         return  j





if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([1, 2, 1, 2, 10, 10, 3]))
