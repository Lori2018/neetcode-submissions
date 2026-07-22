class PrefixTree:
    class Node:
        def __init__(self, data, val):
            self.data = data
            self.val = val
            self.children = [None] * 26

    def __init__(self):
        self.head = self.Node(None, None)
        self.children = [None] * 26

    def insert(self, word: str) -> None:
        node = self.head 
        i = 0
        while i < len(word) and node.children[ord(word[i]) - ord('a')]:
            node = node.children[ord(word[i]) - ord('a')]
            i += 1
        if i < len(word):
            for j in range(i, len(word)):
                node.children[ord(word[j]) - ord('a')] = self.Node(word[j], None)
                node = node.children[ord(word[j]) - ord('a')]
        node.val = 1

    def search(self, word: str) -> bool:
        node = self.head 
        i = 0
        while node and i < len(word): 
            node = node.children[ord(word[i]) - ord('a')]
            i += 1
        return node.val is not None


    def startsWith(self, prefix: str) -> bool:
        node = self.head 
        i = 0
        while node and i < len(prefix):
            node = node.children[ord(prefix[i]) - ord('a')]
            i += 1
        return i == len(prefix) and node is not None
            