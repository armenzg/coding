'''Maximum Number of Non-Overlapping Substrings
Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:

    The substrings do not overlap, that is for any two substrings s[i..j] and s[k..l], either j < k or i > l is true.
    A substring that contains a certain character c must also contain all occurrences of c.

Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in any order.

Example 1:

Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
Explanation: The following are all the possible substrings that meet the conditions:
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.

Example 2:

Input: s = "abbaccd"
Output: ["d","bb","cc"]
Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.

Constraints:

    1 <= s.length <= 10^5
    s contains only lowercase English letters.
'''
from typing import List

def overlap(word, sub1, sub2):
    i = word.find(sub1)
    j = len(sub1) - 1 + i
    k = word.find(sub2)
    l = len(sub2) -1 + k
    return not ((j < k) or (i > l))

def query_word_overlaps(original, word, remaining_words):
    result = False
    for other in remaining_words:
        if overlap(original, word, other):
            result = True
            break
    return result

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        all_occurrences = []
        letters = set()
        for left_index, letter in enumerate(s):
            if not letter in letters:
                letters.add(letter)
                right_index = s.rindex(letter)
                # for i in range(0, left_index):
                #     all_occurrences.append(s[i:right_index])
                # for i in range(right_index, total_len - 1):
                #     all_occurrences.append(s[left_index:right_index+i])
                all_occurrences.append(s[left_index:right_index+1])
        
        # print(all_occurrences)
        do_not_overlap = []
        # Compare each word against all others
        for index, substr in enumerate(all_occurrences):
            if not query_word_overlaps(s, substr, all_occurrences[index+1:]):
                do_not_overlap.append(substr)
        
        return do_not_overlap

sol = Solution()

s = "adefaddaccc"
assert overlap(s, "e", "f") == False
assert overlap(s, "e", "ccc") == False
assert overlap(s, "f", "ccc") == False

s = "abbaccd"
assert overlap(s, "d", "bb") == False
assert overlap(s, "d", "bb") == False
assert overlap(s, "bb", "cc") == False

s = "abab"
sol.maxNumOfSubstrings(s)