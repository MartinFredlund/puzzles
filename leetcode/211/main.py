class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root

        def dfs(node, index):
            if index == len(word):
                return node.is_end_of_word
            if word[index] != ".":
                if word[index] not in node.children:
                    return False
                else:
                    node = node.children[word[index]]
                    return dfs(node, index + 1)
            else:
                is_found = False
                for n in node.children.values():
                    if dfs(n, index + 1):
                        is_found = True
                return is_found

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
