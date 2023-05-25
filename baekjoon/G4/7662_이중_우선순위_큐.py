# #230525
# # heap
# from sys import stdin
# from heapq import heappush, heappop
# new_input = stdin.readline
#
# T = int(new_input())
# for _ in range(T):
#     n = int(new_input())
#     min_heap, max_heap, num_dict = [], [], {}
#     for _ in range(n):
#         command, num = new_input().split()
#         if command == 'I':
#             num = int(num)
#             heappush(min_heap, num)
#             heappush(max_heap, -num)
#             if num_dict.get(num):
#                 num_dict[num] += 1
#             else:
#                 num_dict[num] = 1
#
#         elif num_dict:
#             if num == '-1':
#                 while True:
#                     value = heappop(min_heap)
#                     if num_dict.get(value):
#                         break
#             else:
#                 while True:
#                     value = heappop(max_heap)
#                     if num_dict.get(-value):
#                         value = -value
#                         break
#             if num_dict[value] >= 2:
#                 num_dict[value] -= 1
#             else:
#                 del num_dict[value]
#
#     if num_dict:
#         answer = []
#         while True:
#             value = heappop(max_heap)
#             if num_dict.get(-value):
#                 answer.append(-value)
#                 break
#         while True:
#             value = heappop(min_heap)
#             if num_dict.get(value):
#                 answer.append(value)
#                 break
#
#         print(*answer)
#     else:
#         print('EMPTY')
#
#
# #
# def dual_priority_queue():
#     from sys import stdin
#     from heapq import heappush, heappop
#     new_input = stdin.readline
#
#     T = int(new_input())
#     for _ in range(T):
#         n = int(new_input())
#         min_heap, max_heap, num_dict = [], [], {}
#         for _ in range(n):
#             command, num = new_input().split()
#             if command == 'I':
#                 num = int(num)
#                 heappush(min_heap, num)
#                 heappush(max_heap, -num)
#                 if num_dict.get(num):
#                     num_dict[num] += 1
#                 else:
#                     num_dict[num] = 1
#
#             elif num_dict:
#                 if num == '-1':
#                     while True:
#                         value = heappop(min_heap)
#                         if num_dict.get(value):
#                             break
#                 else:
#                     while True:
#                         value = heappop(max_heap)
#                         if num_dict.get(-value):
#                             value = -value
#                             break
#                 if num_dict[value] >= 2:
#                     num_dict[value] -= 1
#                 else:
#                     del num_dict[value]
#
#         if num_dict:
#             answer = []
#             while True:
#                 value = heappop(max_heap)
#                 if num_dict.get(-value):
#                     answer.append(-value)
#                     break
#             while True:
#                 value = heappop(min_heap)
#                 if num_dict.get(value):
#                     answer.append(value)
#                     break
#
#             print(*answer)
#         else:
#             print('EMPTY')
#
# dual_priority_queue()
#
#
#
# def dual_priority_queue():
#     n = int(new_input())
#     min_heap, max_heap, num_dict = [], [], {}
#     for _ in range(n):
#         command, num = new_input().split()
#         if command == 'I':
#             num = int(num)
#             heappush(min_heap, num)
#             heappush(max_heap, -num)
#             if num_dict.get(num):
#                 num_dict[num] += 1
#             else:
#                 num_dict[num] = 1
#
#         elif num_dict:
#             if num == '-1':
#                 while True:
#                     value = heappop(min_heap)
#                     if num_dict.get(value):
#                         break
#             else:
#                 while True:
#                     value = heappop(max_heap)
#                     if num_dict.get(-value):
#                         value = -value
#                         break
#             if num_dict[value] >= 2:
#                 num_dict[value] -= 1
#             else:
#                 del num_dict[value]
#
#     if num_dict:
#         answer = []
#         while True:
#             value = heappop(max_heap)
#             if num_dict.get(-value):
#                 answer.append(-value)
#                 break
#         while True:
#             value = heappop(min_heap)
#             if num_dict.get(value):
#                 answer.append(value)
#                 break
#
#         return f'{answer[0]} {answer[1]}'
#     return 'EMPTY'
#
# from sys import stdin
# from heapq import heappush, heappop
# new_input = stdin.readline
#
# T = int(new_input())
# for _ in range(T):
#     print(dual_priority_queue())


#
def dual_priority_queue():

    n = int(new_input())
    min_heap, max_heap, num_dict = [], [], {}

    def find_valid_min():
        while True:
            value = heappop(min_heap)
            if num_dict.get(value):
                return value

    def find_valid_max():
        while True:
            value = -heappop(max_heap)
            if num_dict.get(value):
                return value

    for _ in range(n):
        command, num = new_input().split()
        if command == 'I':
            num = int(num)
            heappush(min_heap, num)
            heappush(max_heap, -num)
            if num_dict.get(num):
                num_dict[num] += 1
            else:
                num_dict[num] = 1

        elif num_dict:
            if num == '-1':
                value = find_valid_min()
            else:
                value = find_valid_max()
            if num_dict[value] >= 2:
                num_dict[value] -= 1
            else:
                del num_dict[value]

    if num_dict:
        return f'{find_valid_max()} {find_valid_min()}'

    return 'EMPTY'

from sys import stdin
from heapq import heappush, heappop
new_input = stdin.readline

T = int(new_input())
for _ in range(T):
    print(dual_priority_queue())
