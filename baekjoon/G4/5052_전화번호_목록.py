# 230623
# 250212
# 46744 KB / 736 ms
def main():
    from sys import stdin

    class Node:
        def __init__(self):
            self.children = {}
            self.is_end = False

    class Trie:
        def __init__(self):
            self.head = Node()

        def insert(self, numbers):
            current = self.head
            already = result = False

            for number in numbers:
                if not current.children.get(number):
                    current.children[number] = Node()
                    if already and current.is_end:
                        result = True
                    already = False

                else:
                    already = True
                current = current.children[number]
            current.is_end = True

            return result or already


    new_input = stdin.readline

    T = int(new_input())
    for _ in range(T):
        N = int(new_input())
        phone_list = Trie()
        has_not_sub_str = "YES"
        for _ in range(N):
            if phone_list.insert(new_input().rstrip()):
                has_not_sub_str = "NO"

        print(has_not_sub_str)

main()



# 33432 KB / 164 ms
def main():
    from sys import stdin
    new_input = stdin.readline

    T = int(new_input())
    def determine():
        N = int(new_input())
        phone_list = [new_input().rstrip() for _ in range(N)]
        phone_list.sort()
        for i in range(N - 1):
            ref, phone = phone_list[i:i+2]
            for k in range(len(ref)):
                if ref[k] != phone[k]:
                    break
            else:
                return "NO"

        return "YES"

    for _ in range(T):
        print(determine())

main()