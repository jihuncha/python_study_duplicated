# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false

# Example 4:
#
# Input: s = "([)]"
# Output: false
# Example 5:
#
# Input: s = "{[]}"
# Output: true

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')',
               '{':'}',
               '[':']' }

        if len(s) == 0:
            return True

        for i in s:
            print(i)

Solution().isValid(s)