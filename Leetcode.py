        #1 problem --  "Two Pointers" or "String Manipulation"      date: 03-02-2026

'''
Why this works well:
    Time Complexity: $O(n + m)$, where $n$ and $m$ are the lengths of the two strings.
    We visit every character exactly once.
    Space Complexity: $O(n + m)$ to store the final merged string.
    Efficiency: Using a list (result) and then joining it at the end is more efficient in Python
    than repeated string concatenation, which creates a new string object every time.
'''

class Solution(object):

    def mergeAlternately(self, word1, word2):
        result = []
        max_len = max(len(word1), len(word2))

        for i in range(max_len):
            if i < len(word1):
                result.append(word1[i])

            if i < len(word2):
                result.append(word2[i])

        return"".join(result)

sol = Solution()
##print(sol.mergeAlternately("abcd", "xyz"))
##print(sol.mergeAlternately("Mne  uf", "okyDLfy"))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #2 problem -- "Merge Strings"                                date: 04-02-2026

'''
Why this works:
 Time Complexity: $O(n)$, where $n$ is the length of the string. We look at each character once.
 Space Complexity: $O(1)$, because we only store two integer sums regardless of how long the strings are.
 ord() and chr(): ord() converts a character to its number (e.g., 'a' -> 97), and chr() converts it back.

'''

class solution(object):
    def findTheDifference(self, s, t):

        sum_s=0
        sum_t=0

        for char in s:
            sum_s += ord(char)

        for char in t:
            sum_t += ord(char)

        return chr(sum_t - sum_s)   # for here logic is t-s
    
sol = solution()
##print(sol.findTheDifference("abc", "abcd")) # so range t>s

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  #3 problem --                                 date: 05-02-2026










































