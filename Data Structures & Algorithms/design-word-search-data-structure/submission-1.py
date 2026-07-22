class WordDictionary:
    class Node():
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.children = [None] * 26

    def __init__(self):
        self.head = self.Node(None, None)

    def addWord(self, word: str) -> None:
        i = 0 
        node = self.head 
        while node.children[ord(word[i]) - ord('a')]:
            node = node.children[ord(word[i]) - ord('a')]
            i += 1
        
        while i < len(word):
            node.children[ord(word[i]) - ord('a')] = self.Node(word[i], None)
            print(f"added node {node.key}")
            node = node.children[ord(word[i]) - ord('a')]
            i += 1
        
        print(node.key)
        node.val = 1
        


    def search(self, word: str) -> bool:
        print("SEARCH CALLED")
        return self.searchNode(word, self.head)

    def searchNode(self, word, node): 
        if len(word) == 0:
            return True 
        elif len(word) == 1:
            if word == ".":
                for n in node.children:
                    if n and n.val:
                        return True
                return False
            else:
                return bool(node.children[ord(word) - ord('a')] and node.children[ord(word) - ord('a')].val)

        found = False
        if word[0] == ".":
            for n in node.children:
                if n:
                    found |= self.searchNode(word[1:], n)
            return found
        else:
            if node.children[ord(word[0]) - ord('a')]:
                print(f"matched {word[0]}")
                return self.searchNode(word[1:], node.children[ord(word[0]) - ord('a')])
            return False
