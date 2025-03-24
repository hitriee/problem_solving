# 250318
# 40764 KB / 144 ms
def main():
    def new_sentence(sentence):
        is_blank = False
        result = ''
        for alp in sentence.strip():
            if alp != ' ':
                is_blank = False
                result += alp
            elif not is_blank:
                is_blank = True
                result += alp

        return result


    input_val = input().split('<')[2:-1]
    result = []
    idx = -1

    for element in input_val:
        splited = element.split('>')
        if element[:4] == 'div ':
            title = element.split('"')[1]
            result.append(f'title : {title}')
            idx += 1
        elif splited[0] == 'p':
            result.append(element[2:])
            idx += 1
        elif len(splited) > 1:
            if not element.startswith('/') or splited[0] != '/p':
                result[idx] += splited[1]

    for i in range(len(result)):
        result[i] = new_sentence(result[i])

    return '\n'.join(result)

print(main())




# 40764 KB / 132 ms
def main():
    def new_sentence(sentence):
        is_blank = False
        result = ''
        for alp in sentence.strip():
            if alp != ' ':
                is_blank = False
                result += alp
            elif not is_blank:
                is_blank = True
                result += alp

        return result


    input_val = input().split('<')[2:-1]
    result = []
    idx = -1

    for element in input_val:
        splited = element.split('>')
        if element.startswith('div '):
            title = element.split('"')[1]
            result.append(f'title : {title}')
            idx += 1
        elif splited[0] == 'p':
            result.append(splited[1])
            idx += 1
        elif len(splited) > 1:
            if not element.startswith('/') or splited[0] != '/p':
                result[idx] += splited[1]

    for i in range(len(result)):
        result[i] = new_sentence(result[i])

    return '\n'.join(result)

print(main())





# 40764 KB / 128 ms
def main():
    def new_sentence(sentence):
        is_blank = False
        result = ''
        for alp in sentence.strip():
            if alp != ' ':
                is_blank = False
                result += alp
            elif not is_blank:
                is_blank = True
                result += alp

        return result


    input_val = input().split('<')[2:-1]
    result = []
    idx = -1

    for element in input_val:
        if element.startswith('div '):
            title = element.split('"')[1]
            result.append(f'title : {title}')
            idx += 1
        else:
            splited = element.split('>')

            if splited[0] == 'p':
                result.append(splited[1])
                idx += 1
            elif len(splited) > 1:
                if not element.startswith('/') or splited[0] != '/p':
                    result[idx] += splited[1]

    for i in range(len(result)):
        result[i] = new_sentence(result[i])

    return '\n'.join(result)

print(main())