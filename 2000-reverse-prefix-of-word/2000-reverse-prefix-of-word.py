class Solution:
    def reversePrefix(self , word : str , ch : str):
        if ch not in word:
            return word
        else:
            index = word.index(ch)
            word = list(word)
            left = 0
            right = index

            while left<right:
                word[left] , word[right]  = word[right] , word[left]
                left+=1
                right-=1
            return "".join(word)
            


