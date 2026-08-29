class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.end_of_word = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode() 

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        return True
        
        