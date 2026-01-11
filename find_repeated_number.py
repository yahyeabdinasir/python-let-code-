from typing import  List
from  collections import Counter




class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:


        # this will count the each value how many time is in the our list
        countign = Counter(nums)
        # print(countign)

        for item , counts in countign.items():
            print(counts) # hold the values like the 1,2
            if counts > 1: # checking if the value is greater than 1

                return  item  # but this one returns the pure value that does not has square bracket




        # duplicate = [items for items, count in countign.items() if count > 1]  it can also be use like that the problem is that the retuened value has the square bracket
        # if duplicate :
        #     return duplicate
        # print(countign)



if __name__ == "__main__":
    s = Solution()
    print(s.repeatedNTimes([10, 10, 20, 54]))







