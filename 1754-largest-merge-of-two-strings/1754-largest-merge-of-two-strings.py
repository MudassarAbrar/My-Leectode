class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        res: List[str] = []
        while len(word1) and len(word2):
            if word1 > word2:
                res.append(word1[0])
                word1 = word1[1:]
            else:
                res.append(word2[0])
                word2 = word2[1:]
        res.append(word1)
        res.append(word2)
        return "".join(res)