class Solution:
    def mergeAlternately( self , word1: str , word2: str):
                n, m = len(word1), len(word2)
                merged = [""] * (n + m)
                i = j = k = 0
                while i < n or j < m:
                    if i < n:
                        merged[k] = word1[i]
                        i += 1
                        k += 1
                    if j < m:
                        merged[k] = word2[j]
                        j += 1
                        k += 1
                return "".join(merged)