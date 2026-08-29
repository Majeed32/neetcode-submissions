class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()  

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(i, curr):
            if i == len(word):
                return curr.end_of_word
            char = word[i]
            if char != '.':
                idx = ord(char) - ord('a')
                if not curr.children[idx]:
                    return False
                return dfs(i+1, curr.children[idx])
            for j in range(26):
                if curr.children[j]:
                    check = dfs(i+1, curr.children[j])
                    if check:
                        return True
            return False
        return dfs(0, curr)
                    

            

        
