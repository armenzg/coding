"""
Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + ... + t  (t concatenated with itself 1 or more times)

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

Example 4:

Input: str1 = "ABCDEF", str2 = "ABC"
Output: ""

Constraints:

    1 <= str1.length <= 1000
    1 <= str2.length <= 1000
    str1 and str2 consist of English uppercase letters.


"""
def is_divisible(str1: str, str2: str) -> bool:
    result = False
    len_str1 = len(str1)
    len_str2 = len(str2)
    # str2 % str1
    #    4 % 2 == 0
    #    2 % 4 != 0
    if len_str1 > 0 and len_str2 > 0 and len_str1 % len_str2 == 0:
        for i in range(len_str1//len_str2):
            new_string = str2 * (i+1)
            if str1 == new_string:
                result = True
                break
    return result

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result = ""
        len_str1 = len(str1)
        # Start with longest string
        for i in range(len(str2), 0, -1):
            new_string = str2[0:i]
            if is_divisible(str1, new_string) and is_divisible(str2, new_string):
                result = new_string
                break
        print('"{}"'.format(result), end='')
        return result
    
sol = Solution()
assert sol.gcdOfStrings("ABC", "ABCABC") == "ABC"
assert sol.gcdOfStrings("", "ABC") == ""
assert sol.gcdOfStrings("", "") == ""
assert sol.gcdOfStrings("ABC", "") == ""
assert sol.gcdOfStrings("ABCABC", "ABC") == "ABC"
assert sol.gcdOfStrings("ABABAB", "ABAB") == "AB"
assert sol.gcdOfStrings("LEET", "CODE") == ""
assert sol.gcdOfStrings("ABCDEF", "ABC") == ""