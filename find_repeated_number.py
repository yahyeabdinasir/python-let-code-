from typing import  List
from  collections import Counter




class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:



        countign = Counter(nums)
        for item , counts in countign.items():
            if counts > 1:
                return  item  # but this one returns the pure value that does not has square bracket




        # duplicate = [items for items, count in countign.items() if count > 1]  it can also be use like that the problem is that the retuened value has the square bracket
        # if duplicate :
        #     return duplicate



if __name__ == "__main__":
    s = Solution()
    print(s.repeatedNTimes([10, 10, 20, 54]))







