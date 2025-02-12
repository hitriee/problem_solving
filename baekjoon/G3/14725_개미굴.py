# 250210
# 250212
# 33432 KB / 36 ms
def main():
    from sys import stdin

    class Node:
        def __init__(self):
            self.children = {}
            self.is_end = False
            self.level = 0

    class Trie:
        def __init__(self):
            self.head = Node()

        def insert(self, info):
            current = self.head
            for element in info:
                if not current.children.get(element):
                    current.children[element] = Node()
                current = current.children[element]
            current.is_end = True

        def print(self, key='', level=-1, current=None):
            if current is None:
                current = self.head
            else:
                print(f'{"--"*level}{key}')
            sorted_keys = sorted(current.children)
            for child in sorted_keys:
                self.print(child, level+1, current.children[child])


    new_input = stdin.readline
    N = int(new_input())
    trie = Trie()

    for _ in range(N):
        trie.insert(new_input().split()[1:])

    trie.print()

main()




# 33432 KB / 40 ms
def main():
    from sys import stdin

    class Node:
        def __init__(self):
            self.children = {}

    class Trie:
        def __init__(self):
            self.head = Node()

        def insert(self, info):
            current = self.head
            for element in info:
                if not current.children.get(element):
                    current.children[element] = Node()
                current = current.children[element]

        def print(self, key='', level=-1, current=None):
            if current is None:
                current = self.head
            else:
                print(f'{"--"*level}{key}')
            sorted_keys = sorted(current.children)
            for child in sorted_keys:
                self.print(child, level+1, current.children[child])


    new_input = stdin.readline
    N = int(new_input())
    trie = Trie()

    for _ in range(N):
        trie.insert(new_input().split()[1:])

    trie.print()

main()