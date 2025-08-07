class Solution:
    def mergeAlternately( self , word1: str , word2: str):
        left,right=0,0
        result=[]

        while left < len(word1) or right < len(word2):
            
            if left< len(word1):
                result.append(word1[left])
                left+=1

            if right<len(word2):
                result.append(word2[right])
                right+=1
        return "".join(result)