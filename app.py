from typing import List, Optional
from functools import cache
from math import sqrt, floor
'''
43. Multiple Strings
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
class MultipleStringsSolution:
    def multiply(self, num1: str, num2: str) -> str:
        value = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        result1 = 0
        for digit in num1:
            result1 = 10 * result1 + value[digit]
        result2 = 0
        for digit in num2:
            result2 = 10 * result2 + value[digit]
        return str(result1 * result2)

# A = Solution()
# A.multiply(num1='2456', num2='2345')

'''
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
class TwoSumSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storageMap = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in storageMap:
                return [storageMap[need], i]
            else:
                storageMap[num] = i

# A = TwoSumSolution()
# A.twoSum(nums=[2,7,11,15], target=9)

'''
9. Palindrome Number
An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

Example 1:

Input: x = 121
Output: true
'''
class PalindromSolution:
    def isPalindrome(self, x: int) -> bool:
        #1st way
        lst = []
        for digit in str(x):
            lst.append(digit)

        #2nd way
        r = str(x)
        return r == r[::-1]

# A = PalindromSolution()
# A.isPalindrome(x=-121)

'''
13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
 

Example 1:

Input: s = "III"
Output: 3
'''
class RomanSolution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I' : [1, 'VX', ''],
            'V' : [5, '', 'I'],
            'X' : [10, 'LC', 'I'],
            'L' : [50, '', 'X'],
            'C' : [100, 'DM', 'X'],
            'D' : [500, '', 'C'],
            'M' : [1000, '', 'C']
        }
        val = 0
        lgth = len(s)
        for i, letter in enumerate(s):
            if i != lgth-1 and s[i+1] in roman[letter][1]:
                val = val + (roman[s[i+1]][0] - roman[letter][0])
            elif s[i-1] in roman[letter][2] and i != 0:
                continue
            else:
                val = val + roman[letter][0]
        return val

# A = RomanSolution()
# A.romanToInt(s='CDXXX')

'''
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
'''
class PrefixSolution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i=0
        for s in zip(*strs):
            if len(set(s))!=1: 
                break
            i+=1
                
        return strs[0][0:i]

# A = PrefixSolution()
# A.longestCommonPrefix(strs=["flower","flow","flight"])

'''
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 
Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false
'''
class isValidSolution:
    def isValid(self, s: str) -> bool:
        d = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        temp = []
        for char in s:
            if char in d:
                temp.append(char)
            elif len(temp) >= 1 and char == d[temp.pop()]:
                continue
            else:
                return False
        if len(temp) == 0:
            return True
# A = isValidSolution()
# A.isValid(s="()[]{}")
# A.isValid(s='([)]')

'''
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

Example 1:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MergeTwoSolution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        lst = res
        if not l1 and not l2:
            return l1
        elif l1 and not l2:
            return l1
        elif not l1 and l2:
            return l2
        else:
            while l1 and l2:
                if l1.val <= l2.val:
                    lst.next = l1
                    l1 = l1.next
                elif l2.val < l1.val:
                    lst.next = l2
                    l2 = l2.next
                lst = lst.next
        while l1:
            lst.next = l1
            l1 = l1.next
            lst = lst.next
        while l2:
            lst.next = l2
            l2 = l2.next
            lst = lst.next
        return res.next

# A = MergeTwoSolution()
# A.mergeTwoLists(l1=ListNode([1,2,4]), l2=ListNode([1,3,4]))

'''
96. Unique Binary Search Trees
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1
'''
class NumTreesSolution:
    @cache
    def numTrees(self, n: int) -> int:
        if n <= 1: 
            return 1
        return sum(self.numTrees(i-1) * self.numTrees(n-i) for i in range(1, n+1))

# A = NumTreesSolution()
# A.numTrees(n=1)

'''
28. Implement strStr()
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''
class StrStrSolution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        else:
            return haystack.find(needle)

# A = StrStrSolution()
# A.strStr(haystack='', needle='')

'''
35. Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
'''
class SearchInsertSolution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            close = min(nums, key=lambda x:abs(x-target))
            print(close)
            if close > target:
                return nums.index(close)
            else:
                return nums.index(close) + 1
        
# A = SearchInsertSolution()
# A.searchInsert(nums=[1,3,5,6], target=3)

'''
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''
class MaxSubArraySolution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentMax = nums[0]
        maxSoFar = nums[0]

        for i in range(1, len(nums)):
            currentMax = max(nums[i], currentMax + nums[i])
            maxSoFar = max(currentMax, maxSoFar)
        return maxSoFar

# A = MaxSubArraySolution()
# A.maxSubArray(nums=[1,3,5,-6])

'''
122. Best Time to Buy and Sell Stock II
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve. 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
'''
class MaxProfitSolution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if sorted(prices, reverse=True) == prices:
            return 0
        else:
            for i in range(1, len(prices)):
                profit += max(prices[i]-prices[i-1], 0)
        return profit

# A = MaxProfitSolution()
# A.maxProfit(prices = [1,2,3,4,5])

'''
58. Length of Last Word
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
'''
class LengthOfLastWordSolution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

# A = LengthOfLastWordSolution()
# A.lengthOfLastWord(s="   fly me   to   the moon  ")

'''
69. Sqrt(x)
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
'''
class MySqrtSolution:
    def mySqrt(self, x: int) -> int:
        return floor(sqrt(x))

# A = MySqrtSolution()
# A.mySqrt(x=8)

'''
83. Remove Duplicates from Sorted List
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class DeleteDuplicatesSolution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        print(head.next)
        if not head:
            return None
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
            v = head.val
        return head

# A = DeleteDuplicatesSolution()
# A.deleteDuplicates(head=ListNode([1,1,2]))

class MinStartSolution:
    def minStartValue(self, A: List[int]) -> int:
        total = 0
        res = 0
        for x in A:
            total = total + x
            res = min(res, total)
        return -res + 1

# A = MinStartSolution()
# A.minStartValue(A=[1,2,3,4,-1])

'''
448. Find All Numbers Disappeared in an Array
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
'''
class FindDisappearedNumbersSolution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums)+1)).difference(set(nums)))
        return [i for i in range(1, len(nums)+1) if i not in nums]

# A = FindDisappearedNumbersSolution()
# A.findDisappearedNumbers(nums=[1, 1])

