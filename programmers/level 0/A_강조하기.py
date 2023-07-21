#230721
def solution(myString):
    answer = ''
    for alp in myString:
        if alp == 'a' or alp == 'A':
            answer += 'A'
        else:
            answer += alp.lower()
    return answer