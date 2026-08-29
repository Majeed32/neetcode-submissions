class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            n = len(word)
            res += str(n) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0
        while i < len(s):
            while s[j] != "#":
                j += 1
            word_len = int(s[i : j])
            res.append(s[j+1 : j + word_len+1])
            i = j + word_len + 1
            j = i
        return res
            
