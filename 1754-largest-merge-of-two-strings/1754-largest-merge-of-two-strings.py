class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merged = []
        p1, p2 = 0, 0
        n, m = len(word1), len(word2)

        while p1 < n or p2 < m:
           
            if word1[p1:] > word2[p2:]:
                merged.append(word1[p1])
                p1 += 1
            else:
                merged.append(word2[p2])
                p2 += 1

        return "".join(merged)
