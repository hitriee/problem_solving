#230328
# for
# N = int(input())
# num_arr = list(map(int, input().split()))
# larger_max_len = smaller_max_len = length = 1
#
# for i in range(1, N):
#     if num_arr[i] >= num_arr[i-1]:
#         length += 1
#     else:
#         if larger_max_len < length:
#             larger_max_len = length
#         length = 1
# if larger_max_len < length:
#     larger_max_len = length
#
# length = 1
# for i in range(1, N):
#     if num_arr[i] <= num_arr[i-1]:
#         length += 1
#     else:
#         if smaller_max_len < length:
#             smaller_max_len = length
#         length = 1
# if smaller_max_len < length:
#     smaller_max_len = length
#
# print(max(larger_max_len, smaller_max_len))


# 이중 for
# N = int(input())
# num_arr = list(map(int, input().split()))
# max_len = 1
# for j in range(2):
#     length = 1
#     for i in range(1, N):
#         if num_arr[i-j] >= num_arr[i-1+j]:
#             length += 1
#         else:
#             if max_len < length:
#                 max_len = length
#             length = 1
#     if max_len < length:
#         max_len = length
#
# print(max_len)


#
# N = int(input())
# num_arr = list(map(int, input().split()))
# max_len = length = 1
#
# for i in range(1, N):
#     if num_arr[i] >= num_arr[i-1]:
#         length += 1
#     else:
#         if max_len < length:
#             max_len = length
#         length = 1
# if max_len < length:
#     max_len = length
#
# length = 1
# for i in range(1, N):
#     if num_arr[i] <= num_arr[i-1]:
#         length += 1
#     else:
#         if max_len < length:
#             max_len = length
#         length = 1
# if max_len < length:
#     max_len = length
#
# print(max_len)


# 함수 + 분기
# def return_max():
#     N = int(input())
#     num_arr = list(map(int, input().split()))
#     max_len = 1
#     def find_max(num):
#         nonlocal max_len
#         length = 1
#         if num == 0:
#             for i in range(1, N):
#                 if num_arr[i] >= num_arr[i - 1]:
#                     length += 1
#                 else:
#                     if max_len < length:
#                         max_len = length
#                     length = 1
#         else:
#             for i in range(1, N):
#                 if num_arr[i] <= num_arr[i-1]:
#                     length += 1
#                 else:
#                     if max_len < length:
#                         max_len = length
#                     length = 1
#         if max_len < length:
#             max_len = length
#
#     for j in range(2):
#         find_max(j)
#
#     return max_len
# print(return_max())


# 함수 + for
def return_max():
    N = int(input())
    num_arr = list(map(int, input().split()))
    def find_max():
        max_len = smaller_length = larger_length = 1
        before = num_arr[0]
        for i in range(1, N):
            after = num_arr[i]
            if after > before:
                if smaller_length > max_len:
                    max_len = smaller_length
                smaller_length = 1
                larger_length += 1
            elif after < before:
                if larger_length > max_len:
                    max_len = larger_length
                larger_length = 1
                smaller_length += 1
            else:
                larger_length += 1
                smaller_length += 1
            before = after
        return max(larger_length, smaller_length, max_len)

    return find_max()
print(return_max())