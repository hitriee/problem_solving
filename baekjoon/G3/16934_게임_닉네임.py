# 250211
# 114552 KB / 532 ms
def main():
    from sys import stdin

    class Node(object):
        def __init__(self):
            self.children = {}
            self.cnt = 0

    class Trie(object):
        def __init__(self):
            self.head = Node()

        def insert(self, nickname):
            current = self.head
            new_name = ''
            finished = False

            for alp in nickname:
                if not finished:
                    new_name += alp

                if not current.children.get(alp):
                    if not finished:
                        finished = True

                    current.children[alp] = Node()

                current = current.children[alp]

            current.cnt += 1
            if finished:
                return new_name

            if current.cnt == 1:
                return nickname

            return f'{nickname}{current.cnt}'



    new_input = stdin.readline
    N = int(new_input())
    trie = Trie()
    name_list = [trie.insert(new_input().rstrip()) for _ in range(N)]

    return '\n'.join(name_list)

print(main())


# 114552 KB / 592 ms
def main():
    from sys import stdin

    class Node(object):
        def __init__(self):
            self.children = {}
            self.cnt = 0

    class Trie(object):
        def __init__(self):
            self.head = Node()

        def insert(self, nickname):
            current = self.head
            new_name = ''
            finished = False

            for alp in nickname:
                if not finished:
                    new_name += alp

                if not current.children.get(alp):
                    if not finished:
                        finished = True

                    current.children[alp] = Node()

                current = current.children[alp]

            current.cnt += 1
            if finished or current.cnt == 1:
                return new_name

            return f'{nickname}{current.cnt}'



    new_input = stdin.readline
    N = int(new_input())
    trie = Trie()
    name_list = [trie.insert(new_input().rstrip()) for _ in range(N)]

    return '\n'.join(name_list)

print(main())