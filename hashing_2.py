##Longest Palindrome

'''
If you have a character twice in the array, you can make sure that, you can use that 2 characters in forming the palindrome.

That is the reason, when you see a character which is already in the array, you remove the character, and increment the counter by 2.

If you have still any character in the set, which can increment your length of the word by 1.

i.e aabcbaa

here c is the one which can you use to increment the counter by 1.

'''
class Solution:
    def longestPalindrome(self, s: str) -> int:

        hash_set = set()

        count = 0

        for i in s:
            if i in hash_set:
                hash_set.remove(i)
                count+=2
            else:
                hash_set.add(i)

        if len(hash_set)>0:
            return count+1
        return count



## Contigous sub-array

'''
The concept which I have to remember while solving the solution is

when you see 0, decrement the counter by 1, else increment the counter by 1

and also when you see the running_sum which already existed before the current running_sum, then you can make sure that, the number 1's and 0's are contigous.

Try to see subtract the indices of the currentindex to the index which is already stored in the hash_map, and see if it is the matches the max value.

Edge case: The edgecase, which you have to remember is if storing  the value of hash_map[0] = -1

The example which can make you understand why the edge case is important is  when the array is
0,1,2,3
[0,1,0,1]
-1 0 -1 0

If you just follow the logic without the edge case, then the max value turns out to be only 2.

If you don't want to write the edge case, then you can check by making sure, that if the running_sum becomes 0, then is the current index, is greater than the max_value seen so far.

'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        hash_map = {}
        hash_map[0]=-1
        max_value =0
        running_sum = 0

        for i in range(len(nums)):

            if nums[i]==0:
                running_sum -=1
            else:
                running_sum+=1

            if (running_sum in hash_map):
                max_value = max(max_value, i-hash_map[running_sum])
            else:
                hash_map[running_sum] =i
        return max_value


## Version 2, without prefilling the hash_map.
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        hash_map = {}
        # hash_map[0]=-1
        max_value =0
        running_sum = 0

        for i in range(len(nums)):

            if nums[i]==0:
                running_sum -=1
            else:
                running_sum+=1

            if running_sum ==0:
                max_value = max(max_value, i+1)

            if (running_sum in hash_map):
                max_value = max(max_value, i-hash_map[running_sum])
            else:
                hash_map[running_sum] =i
        return max_value



'''
The concept of the problem is based on the underlying statement, if you remove the required target from the running sum,
If that value already existed in the running_sum then you can count as one of your required sub array.

Edge case: hash_map[0]=1

Why?

Consider the example

4, 3, 7 and K=7

Answer : 2

One sub array is [4,3] and the other one is [7]

If you dont place hash_map[0]=1, you will get only one.

I m using defaultdict(int) so that the hash_map gets initialized with 0 by default.

'''

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = defaultdict(int)

        hash_map[0]=1

        running_sum =0

        max_sub_arrays = 0

        for i in nums:

            running_sum+=i

            if running_sum-k in hash_map:
                max_sub_arrays+= hash_map[running_sum-k]

            hash_map[running_sum]+=1


        return max_sub_arrays


