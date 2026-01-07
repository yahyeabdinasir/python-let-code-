from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # # initialising the empty set
        # seen = set()
        #
        # # iterate over the nms
        # for num in nums:
        #     # if the nums is seen in the seen return True
        #
        #     if num in seen:
        #         # we found the duplicated
        #         return  True
        #
        #
        #    # if not found the first iterarion keep up till u finish the iteration
        #
        #     else :
        #         seen.add(num)
        #
        #
        # # return falso when no duplicate is found in the seen
        # return False


        n = len(nums)
        #the lengeth of the nums


        for i in range(n-1):# iterate over the nums legeth and substract  -1 and that it's (0,3) 0,1,3
            for j in range(i+1 , n): # ineer loop add each outer loop +1  with n and the value of 0 is 3 and 2, 3 and 3 is 3
                if nums[i] == nums[j]:   # so now  check them each value is duplicated or not
                    return  True
        return False





if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1, 3, 20,  1]))
















#
# for i in range(2):
#     print(i , end=" ")
#     for j in range(1,6):
#         print(j , end= " ")
#     print()
