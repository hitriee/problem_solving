# #230606
# def find_cnt_leaf_node():
#     N = int(input())
#     parent = list(map(int, input().split()))
#     selected = int(input())
#     children = [[] for _ in range(N)]
#     root = -1 # 루트 노드
#     for i in range(N):
#         if parent[i] != -1:
#             children[parent[i]].append(i)
#         else:
#             root = i
#
#     if selected == root: # 선택된 노드가 루트 노드일 경우
#         return 0
#
#     cnt_leaf = 0 # 현재 리프노드의 개수
#     for i in range(N):
#         if not children[i]:
#             cnt_leaf += 1
#
#     if not children[selected]: # 선택된 노드가 리프 노드일 경우
#         cnt_leaf -= 1
#     else:
#         # 선택된 노드에 달린 리프 노드 개수 차감
#         from collections import deque
#         q = deque()
#         q.append(selected)
#         while q:
#             node = q.popleft()
#             if not children[node]:
#                 cnt_leaf -= 1
#             else:
#                 for i in children[node]:
#                     q.append(i)
#
#     length = len(children[parent[selected]])
#     # 선택된 노드의 부모 노드의 자식이 선택된 노드 외에도 존재한다면, 리프 노드 개수 출력
#     if length > 1:
#         return cnt_leaf
#     # 선택된 노드의 부모 노드의 자식이 선택된 노드뿐이라면, 부모 노드가 새로운 리프 노드가 됨 (+1)
#     return cnt_leaf + 1
#
#
# print(find_cnt_leaf_node())
#
#
# #
# def find_cnt_leaf_node():
#     N = int(input())
#     parent = list(map(int, input().split()))
#     selected = int(input())
#     if parent[selected] == -1: # 선택된 노드가 루트 노드일 경우
#         return 0
#
#     children = [[] for _ in range(N)] # 노드별 자식 노드
#     for i in range(N):
#         if parent[i] != -1:
#             children[parent[i]].append(i)
#
#     cnt_leaf = 0 # 현재 리프노드의 개수
#     for i in range(N):
#         if not children[i]:
#             cnt_leaf += 1
#
#     if not children[selected]: # 선택된 노드가 리프 노드일 경우
#         cnt_leaf -= 1
#     else:
#         # 선택된 노드에 달린 리프 노드 개수 차감
#         from collections import deque
#         q = deque()
#         q.append(selected)
#         while q:
#             node = q.popleft()
#             if not children[node]:
#                 cnt_leaf -= 1
#             else:
#                 for i in children[node]:
#                     q.append(i)
#
#     length = len(children[parent[selected]])
#     # 선택된 노드의 부모 노드의 자식이 선택된 노드 외에도 존재한다면, 리프 노드 개수 출력
#     if length > 1:
#         return cnt_leaf
#     # 선택된 노드의 부모 노드의 자식이 선택된 노드뿐이라면, 부모 노드가 새로운 리프 노드가 됨 (+1)
#     return cnt_leaf + 1
#
#
# print(find_cnt_leaf_node())
#
#
# #
# def find_cnt_leaf_node():
#     N = int(input())
#     parent = list(map(int, input().split()))
#     selected = int(input())
#     if parent[selected] == -1: # 선택된 노드가 루트 노드일 경우
#         return 0
#
#     children = [[] for _ in range(N)] # 노드별 자식 노드
#     for i in range(N):
#         if parent[i] != -1:
#             children[parent[i]].append(i)
#
#     cnt_leaf = 0 # 현재 리프노드의 개수
#     for i in range(N):
#         if not children[i]:
#             cnt_leaf += 1
#
#     if not children[selected]: # 선택된 노드가 리프 노드일 경우
#         cnt_leaf -= 1
#     else:
#         def bfs():
#             nonlocal cnt_leaf
#             # 선택된 노드에 달린 리프 노드 개수 차감
#             from collections import deque
#             q = deque()
#             q.append(selected)
#             while q:
#                 node = q.popleft()
#                 if not children[node]:
#                     cnt_leaf -= 1
#                 else:
#                     for i in children[node]:
#                         q.append(i)
#         bfs()
#     length = len(children[parent[selected]])
#     # 선택된 노드의 부모 노드의 자식이 선택된 노드 외에도 존재한다면, 리프 노드 개수 출력
#     if length > 1:
#         return cnt_leaf
#     # 선택된 노드의 부모 노드의 자식이 선택된 노드뿐이라면, 부모 노드가 새로운 리프 노드가 됨 (+1)
#     return cnt_leaf + 1
#
#
# print(find_cnt_leaf_node())
#
#
#
def find_cnt_leaf_node():
    N = int(input())
    parent = list(map(int, input().split()))
    selected = int(input())
    if parent[selected] == -1: # 선택된 노드가 루트 노드일 경우
        return 0

    children = [[] for _ in range(N)] # 노드별 자식 노드
    root = -1
    for i in range(N):
        if parent[i] != -1:
            children[parent[i]].append(i)
        else:
            root = i


    def bfs():
        from collections import deque

        cnt_leaf, parent_selected = 0, parent[selected]
        # 선택된 노드에 달린 리프 노드 제외한 리프 노드 찾기
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not children[node]:
                cnt_leaf += 1
            elif node == parent_selected:
                if len(children[node]) == 1:
                    cnt_leaf += 1
                else:
                    for i in children[node]:
                        if i != selected:
                            q.append(i)
            else:
                for i in children[node]:
                    q.append(i)

        return cnt_leaf

    return bfs()


print(find_cnt_leaf_node())