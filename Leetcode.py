        #1 problem

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
print(sol.mergeAlternately("abcd", "xyz"))
print(sol.mergeAlternately("Mne  uf", "okyDLfy"))

    #2 problem
