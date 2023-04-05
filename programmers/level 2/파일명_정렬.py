#230405
# 구현, 정렬
def solution(files):
    file_list = []
    for file in files:
        splited_file = []
        start = 0
        for i in range(len(file)):
            element = file[i]
            if element.isdigit():
                if start == 0:
                    splited_file.append(file[:i])
                    start = i
            elif len(splited_file) == 1:
                splited_file.append(file[start:i])
                start = i
        splited_file.append(file[start:])
        file_list.append(splited_file[:])
    file_list.sort(key= lambda file: (file[0].lower(), int(file[1])))
    file_list = list(map(''.join, file_list))
    return file_list
'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (3.00ms, 10.9MB)
테스트 4 〉	통과 (2.96ms, 10.7MB)
테스트 5 〉	통과 (2.90ms, 10.5MB)
테스트 6 〉	통과 (2.76ms, 10.5MB)
테스트 7 〉	통과 (2.61ms, 10.6MB)
테스트 8 〉	통과 (2.58ms, 10.7MB)
테스트 9 〉	통과 (2.51ms, 10.7MB)
테스트 10 〉	통과 (2.71ms, 10.6MB)
테스트 11 〉	통과 (2.61ms, 10.5MB)
테스트 12 〉	통과 (2.88ms, 10.7MB)
테스트 13 〉	통과 (2.60ms, 10.6MB)
테스트 14 〉	통과 (6.00ms, 10.8MB)
테스트 15 〉	통과 (5.55ms, 10.8MB)
테스트 16 〉	통과 (2.71ms, 10.7MB)
테스트 17 〉	통과 (2.27ms, 10.6MB)
테스트 18 〉	통과 (2.24ms, 10.4MB)
테스트 19 〉	통과 (2.71ms, 10.8MB)
테스트 20 〉	통과 (2.70ms, 10.5MB)
'''


# break
def solution(files):
    file_list = []
    for file in files:
        splited_file = []
        start = 0
        for i in range(len(file)):
            element = file[i]
            if element.isdigit():
                if start == 0:
                    splited_file.append(file[:i])
                    start = i
            elif start:
                splited_file.append(file[start:i])
                start = i
                break
        splited_file.append(file[start:])
        file_list.append(splited_file[:])
    file_list.sort(key= lambda file: (file[0].lower(), int(file[1])))
    file_list = list(map(''.join, file_list))
    return file_list
'''
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.3MB)
테스트 2 〉	통과 (0.05ms, 10.4MB)
테스트 3 〉	통과 (2.41ms, 10.8MB)
테스트 4 〉	통과 (3.32ms, 10.8MB)
테스트 5 〉	통과 (2.51ms, 10.5MB)
테스트 6 〉	통과 (4.12ms, 10.7MB)
테스트 7 〉	통과 (2.31ms, 10.5MB)
테스트 8 〉	통과 (2.16ms, 10.7MB)
테스트 9 〉	통과 (2.09ms, 10.8MB)
테스트 10 〉	통과 (2.26ms, 10.5MB)
테스트 11 〉	통과 (2.20ms, 10.6MB)
테스트 12 〉	통과 (4.10ms, 10.6MB)
테스트 13 〉	통과 (2.79ms, 10.4MB)
테스트 14 〉	통과 (3.59ms, 10.8MB)
테스트 15 〉	통과 (2.96ms, 10.8MB)
테스트 16 〉	통과 (2.50ms, 10.7MB)
테스트 17 〉	통과 (2.26ms, 10.6MB)
테스트 18 〉	통과 (3.46ms, 10.5MB)
테스트 19 〉	통과 (2.94ms, 10.8MB)
테스트 20 〉	통과 (2.35ms, 10.9MB)
'''

# 변수에 할당X
def solution(files):
    file_list = []
    for file in files:
        splited_file = []
        start = 0
        for i in range(len(file)):
            element = file[i]
            if element.isdigit():
                if start == 0:
                    splited_file.append(file[:i])
                    start = i
            elif len(splited_file) == 1:
                splited_file.append(file[start:i])
                start = i
        splited_file.append(file[start:])
        file_list.append(splited_file[:])
    file_list.sort(key= lambda file: (file[0].lower(), int(file[1])))
    return list(map(''.join, file_list))
'''
정확성  테스트
테스트 1 〉	통과 (0.07ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.3MB)
테스트 3 〉	통과 (3.65ms, 10.7MB)
테스트 4 〉	통과 (5.06ms, 10.9MB)
테스트 5 〉	통과 (2.89ms, 10.5MB)
테스트 6 〉	통과 (4.55ms, 10.6MB)
테스트 7 〉	통과 (2.64ms, 10.6MB)
테스트 8 〉	통과 (2.43ms, 10.8MB)
테스트 9 〉	통과 (2.62ms, 10.7MB)
테스트 10 〉	통과 (4.63ms, 10.7MB)
테스트 11 〉	통과 (2.65ms, 10.6MB)
테스트 12 〉	통과 (5.76ms, 10.9MB)
테스트 13 〉	통과 (2.90ms, 10.6MB)
테스트 14 〉	통과 (5.35ms, 10.8MB)
테스트 15 〉	통과 (10.61ms, 10.7MB)
테스트 16 〉	통과 (5.00ms, 10.7MB)
테스트 17 〉	통과 (2.32ms, 10.4MB)
테스트 18 〉	통과 (2.29ms, 10.7MB)
테스트 19 〉	통과 (2.61ms, 10.7MB)
테스트 20 〉	통과 (3.06ms, 10.7MB)
'''