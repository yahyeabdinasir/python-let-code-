from typing import List
class Solution:
    def sum_of_even(self, nums: List[int]) -> int:





        total = 0
        for n in nums:

            if n%2==0:
               total +=n
        return  total




# we can also get the odoo values

        # total = 0
        # for n in nums:
        #     if n % 2 == 1:
        #         total += n
        # return total


if __name__ == "__main__":
    s = Solution()
    print(s.sum_of_even([1, 2, 1, 2, 10]))




# and this better approach and it can be applied  also can be applied
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         result = 0
#         for n in nums:
#             result ^= n
#         return result
