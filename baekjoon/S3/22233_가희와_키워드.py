#230506
# set
from sys import stdin
def new_input(): return stdin.readline().rstrip()
N, M = map(int, new_input().split())
memo_pad = set(new_input() for _ in range(N))
blog = [set(new_input().split(',')) for _ in range(M)]
for keywords in blog:
    memo_pad -= keywords
    print(len(memo_pad))


# 함수화
def cnt_remain():
    from sys import stdin
    def new_input(): return stdin.readline().rstrip()
    N, M = map(int, new_input().split())
    memo_pad = set(new_input() for _ in range(N))
    blog = [set(new_input().split(',')) for _ in range(M)]
    for keywords in blog:
        memo_pad -= keywords
        print(len(memo_pad))
cnt_remain()


# blog X
def cnt_remain():
    from sys import stdin
    def new_input(): return stdin.readline().rstrip()
    N, M = map(int, new_input().split())
    memo_pad = set(new_input() for _ in range(N))
    for _ in range(M):
        keywords = set(new_input().split(','))
        memo_pad -= keywords
        print(len(memo_pad))
cnt_remain()


# difference_update
def cnt_remain():
    from sys import stdin
    def new_input(): return stdin.readline().rstrip()
    N, M = map(int, new_input().split())
    memo_pad = set(new_input() for _ in range(N))
    for _ in range(M):
        keywords = set(new_input().split(','))
        memo_pad.difference_update(keywords)
        print(len(memo_pad))
cnt_remain()


# 함수화 X
from sys import stdin
def new_input(): return stdin.readline().rstrip()
N, M = map(int, new_input().split())
memo_pad = set(new_input() for _ in range(N))
for _ in range(M):
    keywords = set(new_input().split(','))
    memo_pad.difference_update(keywords)
    print(len(memo_pad))


# keywords X
def cnt_remain():
    from sys import stdin
    def new_input(): return stdin.readline().rstrip()
    N, M = map(int, new_input().split())
    memo_pad = set(new_input() for _ in range(N))
    for _ in range(M):
        memo_pad -= set(new_input().split(','))
        print(len(memo_pad))
cnt_remain()


# set() => for
def cnt_remain():
    from sys import stdin
    def new_input(): return stdin.readline().rstrip()
    N, M = map(int, new_input().split())
    memo_pad = set()
    for _ in range(N):
        memo_pad.add(new_input())
    for _ in range(M):
        memo_pad -= set(new_input().split(','))
        print(len(memo_pad))
cnt_remain()
