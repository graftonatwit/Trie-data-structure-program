class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        
        def insert(root, key):
            curr=root
            
            for c in key:
                index = ord(c)-ord('a')
                if curr.children[index] is None:
                    new_node = TrieNode()
                    curr.children[index] = new_node
                curr = curr.children[index]
            curr.isEndOfWord = True
            
        def search(root, key):
            curr = root
            for c in key:
                index = ord(c)-ord('a')
                if curr.children[index] is None:
                    return False
                curr = curr.children[index]
            return curr.isEndOfWord
        
        def delete(root, key, depth=0):
            if root is None:
                return None
            if depth == len(key):
                if root.isEndOfWord:
                    root.isEndOfWord = False
                if (all(child is None for child in root.children)):
                    return None
                return root
            index = ord(key[depth]) - ord('a')
            root.children[index] = delete(root.children[index], key, depth + 1)
            if not root.isEndOfWord and (all(child is None for child in root.children)):
                return None
            return root
            
        insertWords = ['art', 'arts', 'ars', 'ra', 'rar', 'tar', 'tars', 'tart']
        for word in insertWords:
            insert(root, word)
        deleteWords = ['rar', 'tar', 'tars']
        for word in deleteWords:
            root = delete(root, word)
        print(search(root, 'art'))
        print(search(root, 'arts'))
        print(search(root, 'ars'))
        print(search(root, 'ra'))
        print(search(root, 'rar'))
        