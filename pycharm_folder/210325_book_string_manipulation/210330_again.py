#1. palindrome

# Example 1:
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.


import collections
from typing import Deque, List, re

# s = "A man, a plan, a canal: Panama"
# s = "race a car"
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # deque: Deque = collections.deque()
#         q = collections.deque()
#
#         for char in s:
#             if char.isalnum():
#                 q.append(char.lower())
#
#         print(q)
#         while len(q) > 1:
#             if q.popleft() != q.pop():
#                 return False
#         return True
#
# print(Solution().isPalindrome(s))


###########################################################################################################################################
# Example 1:
#
# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# Explanation:
# The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
# Example 2:
#
# Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
# logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
#
# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         letters, digits = [],[]
#         print(logs)
#
#         for check_all in logs:
#             if check_all.split()[1].isdigit():
#                 digits.append(check_all)
#             else:
#                 letters.append(check_all)
#
#         letters.sort(key=lambda x: [x.split()[1:], x.split()[0]])
#
#         return letters + digits
#
# print(Solution().reorderLogFiles(logs))

# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
# Explanation:
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"),
# and that "hit" isn't the answer even though it occurs more because it is banned.
# Example 2:
#
# Input: paragraph = "a.", banned = []
# Output: "a"

# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# 
# import re
# import collections
# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
#             .lower().split()
#             if word not in banned]
#         # print(words)
# 
#         print(collections.Counter(words).most_common(1))
# 
# Solution().mostCommonWord(paragraph, banned)

# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Example 2:
#
# Input: strs = [""]
# Output: [[""]]

# strs = ["eat","tea","tan","ate","nat","bat"]
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         dic = {}
#
#         for i in strs:
#             temp_str = ''.join(sorted(i))
#             print(temp_str)
#             if temp_str not in dic:
#                 dic[temp_str] = [i]
#             else:
#                 dic[temp_str].append(i)
#         return list(dic.values())
#
#
# print(Solution().groupAnagrams(strs))

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"
# Example 3:
#
# Input: s = "a"
# Output: "a"
# Example 4:
#
# Input: s = "ac"
# Output: "a"

# import collections
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         collections.deque =

# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# s = "babad"
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         m = ''
#         for i in range(len(s)):
#             for j in range(len(s), i,-1):
#                 if len(m) >= j - i:  # To reduce time
#                     break
#                 elif s[i:j] == s[i:j][::-1]:
#                     m = s[i:j]
#                     break
#         return m
#
# print(Solution().longestPalindrome(s))

# s = "abcdedcbabs"
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         print(s[0:8])
#         def expand(left : int, right: int) -> str:
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 print(s[left], s[right])
#                 left -= 1
#                 right += 1
#             print("expand_result - {}".format(s[left+1:right]))
#             return s[left + 1:right]
#
#         if len(s) < 2 or s == s[::-1]:
#             return s
#
#         result = ''
#         # index 니까 -1 해줌
#         for i in range(len(s) - 1):
#             result = max(result, expand(i, i+1), expand(i, i+2), key=len)
#             print("i - {}, result - {}".format(i, result))
#         return result
#
# print(Solution().longestPalindrome(s))

# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
#
height = [4,2,0,3,2,5]
# Output: 9

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

            if not len(stack):
                break

            # ??? 이전과의 차이만큼 물 높이 처리?
            distance = i - stack[-1] -1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)


        # if not height:
        #     return 0
        #
        # left, right = 0, len(height) - 1
        # left_max, right_max = height[left], height[right]
        # volume = 0
        #
        # while left < right:
        #     if left_max < right_max:
        #         left += 1
        #         if left_max - height[left] > 0:
        #             volume += left_max - height[left]
        #         left_max = max(left_max, height[left])
        #     else :
        #         right -= 1
        #         if right_max - height[right] > 0:
        #             volume += right_max - height[right]
        #         right_max = max(right_max, height[right])
        #
        # return volume

print(Solution().trap(height))
