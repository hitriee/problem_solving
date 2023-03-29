#230329
# 구현

# 1보다 큰 수일 때 다른 수 곱해서 최댓값 찾기 - 시간 많이 걸림
# from sys import stdin
# to_float = lambda : float(stdin.readline().rstrip())
# N = int(stdin.readline().rstrip())
# max_num = 0
# nums = [to_float() for _ in range(N)]
# for i in range(N):
#     num = nums[i]
#     if num > max_num:
#         max_num = num
#     if num > 1:
#         for j in range(i+1, N):
#             num *= nums[j]
#             if num > max_num:
#                 max_num = num
# print(f'{max_num :.3f}')


# 그 전 수보다 작으면 들어가지 않음
# from sys import stdin
# to_float = lambda : float(stdin.readline().rstrip())
# N = int(stdin.readline().rstrip())
# max_num = 0
# nums = [to_float() for _ in range(N)]
# before = 0
# for i in range(N):
#     num = nums[i]
#     if num > max_num:
#         max_num = num
#     if num > 1 and num > before:
#         for j in range(i+1, N):
#             num *= nums[j]
#             if num > max_num:
#                 max_num = num
#     before = num
# print(f'{max_num :.3f}')

# 그 전 수까지의 곱보다 작으면 들어가지 않음
# from sys import stdin
# to_float = lambda : float(stdin.readline().rstrip())
# N = int(stdin.readline().rstrip())
# max_num = 0
# nums = [to_float() for _ in range(N)]
# before = 1
# for i in range(N):
#     num = nums[i]
#     if num > max_num:
#         max_num = num
#     if num > 1 and num > before:
#         for j in range(i+1, N):
#             num *= nums[j]
#             if num > max_num:
#                 max_num = num
#     before *= num
# print(f'{max_num :.3f}')


# 1과 그 전 수 중 큰 것보다 작으면 들어가지 않음
# from sys import stdin
# to_float = lambda : float(stdin.readline().rstrip())
# N = int(stdin.readline().rstrip())
# max_num = 0
# nums = [to_float() for _ in range(N)]
# before = 1
# for i in range(N):
#     num = nums[i]
#     if num > max_num:
#         max_num = num
#     if num > before:
#         for j in range(i+1, N):
#             num *= nums[j]
#             if num > max_num:
#                 max_num = num
#     before = max(num, 1)
# print(f'{max_num :.3f}')

# 함수형
# def return_max_num():
#     from sys import stdin
#     to_float = lambda : float(stdin.readline().rstrip())
#     N = int(stdin.readline().rstrip())
#     max_num, before = 0, 1
#     nums = [to_float() for _ in range(N)]
#     for i in range(N):
#         num = nums[i]
#         if num > max_num:
#             max_num = num
#         if num > before:
#             for j in range(i+1, N):
#                 num *= nums[j]
#                 if num > max_num:
#                     max_num = num
#         before = max(num, 1)
#     return f'{max_num :.3f}'
# print(return_max_num())


# 곱한 값이 1보다 작으면 종료
# def return_max_num():
#     from sys import stdin
#     to_float = lambda : float(stdin.readline().rstrip())
#     N = int(stdin.readline().rstrip())
#     max_num, before = 0, 1
#     nums = [to_float() for _ in range(N)]
#     for i in range(N):
#         num = nums[i]
#         if num > max_num:
#             max_num = num
#         if num > before:
#             for j in range(i+1, N):
#                 num *= nums[j]
#                 if num > max_num:
#                     max_num = num
#                 if num < 1:
#                     break
#         before = max(num, 1)
#     return f'{max_num :.3f}'
# print(return_max_num())


# 입력 시 최댓값 갱신
def return_max_num():
    from sys import stdin
    to_float = lambda : float(stdin.readline().rstrip())
    N = int(stdin.readline().rstrip())
    max_num, before = 0, 1
    nums = []
    for _ in range(N):
        nums.append(to_float())
        if nums[-1] > max_num:
            max_num = nums[-1]
    for i in range(N):
        num = nums[i]
        if num > before:
            for j in range(i+1, N):
                num *= nums[j]
                if num > max_num:
                    max_num = num
                if num < 1:
                    break
        before = max(num, 1)
    return f'{max_num :.3f}'
print(return_max_num())