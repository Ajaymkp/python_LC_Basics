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
##print(sol.findTheDifference("abc", "abcd")) # have to range t>s

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  #3 problem -- Substring Search                                date: 05-02-2026

'''

The Logic (Sliding Window)
Calculate the length of the needle (let's call it n) and haystack (let's call it h).

1.Loop through the haystack from index 0 up to h - n.

2. At each step i, check if the "slice" haystack[i : i+n] is equal to needle.

3. If yes, return i.

4. If the loop finishes without finding it, return -1.

'''

class solution(object):
    def strStr(self, haystack, needle):
        
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # if needle is longer than haystack, it can't fit

        if len(needle) > len(haystack):
            return -1

        # we only need to check up to the point where
        # the needle can fit into the haystack

        for i in range(len(haystack) - len(needle) + 1):

            #check the slice of haystack against the needle
            if haystack[i : i+ len(needle)] == needle:
                return i
            
        return -1
           

sol = solution()
##print(sol.strStr("sadbutsad", "sad"))
##print(sol.strStr("leetcode", "leeto"))
##print(sol.strStr("sad", "sadd"))
'''                       
           
h="sadbutsad"
n="sad"
for i in range(len(h) - len(n) + 1):   # means in list last value not be print so +1 needed
    
    print(h[i : i+ len(n)])  # for here to print full sad     if not op will sa
'''       
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



  #4 problem --  Valid Anagram                              date: 06-02-2026
'''This is the preferred solution for interviews. We count the frequency of every character.
  If s has three 'a's, t must also have three 'a's.
  Time Complexity: $O(N)$ (faster than sorting).
  Space Complexity: $O(1)$ (since there are only 26 lowercase letters).
'''

class solution(object):
    def isAnagaram(self, s, t):

        if len(t) != len(s):
            return False
        count_s = {}
        count_t = {}
        
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        return count_t == count_s
sol = solution()
##print(sol.isAnagaram("anagram", "nagaram"))
##print(sol.isAnagaram("cat", "tar"))


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


       #5 problem --   Repeated Substring pattern                            date: 07-02-2026
'''
The "Clever" Approach (String Math)If a string s is made of a repeating pattern (like "abab"), then s is essentially P + P.
  If we create a new string by adding s to itself (s + s), we get P + P + P + P.
  If we remove the very first and very last characters of this new doubled string,
  the original s (P + P) should still be visible somewhere in the middle.If s is not a pattern (like "aba"), this trick won't work.
    Time Complexity: $O(N)$ (very fast).
    Space Complexity: $O(N)$ (to store the doubled string).
'''
class solution(object):
    def repeatedSubstringPattern(self, s):
        doubled = s+s
        trimmed = doubled[1:-1]
        return s in trimmed
        
##print(solution().repeatedSubstringPattern("abab"))

##s="abab"        
##doubled = s+s
##trimmed = doubled[1:-1]
##print(doubled)
##print(trimmed)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

       #6 problem --                                date: 08-02-2026
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

       #7 problem --                                date: 09-02-2026

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

       #8 problem --                                date: 10-02-2026
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


      #9 problem --                                 date: 11-02-2026

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

      #10 problem --                                date: 12-02-2026

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



