from typing import List



# class Solution:
#     def twoSum(slef, nums: List[int], target):#(0,3)
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):#(1,3)
#                 if nums[i] + nums[j] == target:
#                     return i, j
#
#
# if __name__ == "__main__":
#     s = Solution()
#     print(s.twoSum([10, 50, 20], 30))    # [0, 1]
# #     print(s.twoSum([2, 7, 11, 15], 9))   # [0, 1]


# names = ['yahye' , 'farah' , 'abdi ' , 'muhubo']
# for word in names:
#     print(word , len(word))
#

# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
#
#
# for user , status in users.copy().items():
#     print(user)
#     # print(status)
#     if status == 'inactive':
#         print(users[user])
#         # del users[user]
#         # print(users,status)
#
# fo_active_user = {}
# for user , status in users.items():
#     if status == "active":
#       fo_active_user[user] = status
# print(fo_active_user)
#

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for words in a :
#     print(words , len(words))
#
# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for words in range(len(a)) :
#     print(words , a[words])
#




for n in range(2,10):
    for x in range(2,n):
        if n % x ==0 :
            print(f"this {n} and  {x} * {n//x}")
            break





































