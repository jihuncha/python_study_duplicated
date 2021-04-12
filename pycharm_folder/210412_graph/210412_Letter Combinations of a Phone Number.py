from typing import List

digits = "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
#
# digits = ""
# Output: []
#
# digits = "2"
# Output: ["a", "b", "c"]


import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '1': [],
            '2': ['a','b','c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            '10': [],
        }

        def dfs(input_num: str) -> List:
            temp = []

            for data in input_num:
                if not mapping[data]:
                    continue
                for j in mapping[data]:
                    temp.append(j)
            return temp

print(Solution().letterCombinations(digits))

