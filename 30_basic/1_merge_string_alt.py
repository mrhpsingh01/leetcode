class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word_switcher = True
        loop = True
        i=0
        j=0
        result = ""
        while loop:
            if i < len(word1) and word_switcher:
                result = result+word1[i]
                word_switcher = False
                i+=1
            elif j< len(word2):
                result = result+word2[j]
                word_switcher = True
                j+=1
            else:
                if i < len(word1):
                    word_switcher=True
                else:
                    loop = False
        return result


word1 = "abcd"
word2 = "pq"

x = Solution().mergeAlternately(word1,word2)

print(x)