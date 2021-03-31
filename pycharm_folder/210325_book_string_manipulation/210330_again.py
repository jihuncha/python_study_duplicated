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


