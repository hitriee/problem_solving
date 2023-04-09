#230409
# 구현, 파싱
while True:
    try:
        dance_values = input()
        errors = set()
        dance_list = dance_values.split()
        N = len(dance_list)
        has_twirl = has_hop = has_dip = False
        for i in range(N):
            dance_value = dance_list[i]
            if dance_value == 'dip':
                has_dip = True
                if i+1 < N and dance_list[i+1] == 'twirl':
                    has_twirl = True
                else:
                    for di in range(-1, -3, -1):
                        ni = i+di
                        if ni >= 0 and dance_list[ni] == 'jiggle':
                            break
                    else:
                        errors.add('1')
                        dance_list[i] = dance_value.upper()
            elif dance_value == 'twirl' and not has_twirl:
                has_twirl = True
            elif dance_value == 'hop' and not has_hop:
                has_hop = True
        if not dance_values.endswith('clap stomp clap'):
            errors.add('2')
        if has_twirl and not has_hop:
            errors.add('3')
        if dance_list[0] == 'jiggle':
            errors.add('4')
        if not has_dip:
            errors.add('5')
        length = len(errors)
        new_dance_values = ' '.join(dance_list)
        if length == 0:
            print(f'form ok: {new_dance_values}')
        elif length == 1:
            print(f'form error {errors.pop()}: {new_dance_values}')
        else:
            sorted_errors = sorted(errors)
            str_errors = ', '.join(sorted_errors[:-1]) + ' and ' + sorted_errors[-1]
            print(f'form errors {str_errors}: {new_dance_values}')
    except Exception:
        break

# 함수화
def has_error():
    def error_test():
        nonlocal errors
        dance_list = dance_values.split()
        N = len(dance_list)
        has_twirl = has_hop = has_dip = False

        for i in range(N):
            dance_value = dance_list[i]
            if dance_value == 'dip':
                has_dip = True
                if i + 1 < N and dance_list[i + 1] == 'twirl':
                    has_twirl = True
                else:
                    for di in range(-1, -3, -1):
                        ni = i + di
                        if ni >= 0 and dance_list[ni] == 'jiggle':
                            break
                    else:
                        errors.add('1')
                        dance_list[i] = dance_value.upper()
            elif dance_value == 'twirl' and not has_twirl:
                has_twirl = True
            elif dance_value == 'hop' and not has_hop:
                has_hop = True

        if not dance_values.endswith('clap stomp clap'):
            errors.add('2')
        if has_twirl and not has_hop:
            errors.add('3')
        if dance_list[0] == 'jiggle':
            errors.add('4')
        if not has_dip:
            errors.add('5')
        return ' '.join(dance_list)

    errors = set()
    new_dance_values = error_test()
    length = len(errors)
    if length == 0:
        return f'form ok: {new_dance_values}'
    elif length == 1:
        return f'form error {errors.pop()}: {new_dance_values}'
    else:
        sorted_errors = sorted(errors)
        str_errors = ', '.join(sorted_errors[:-1]) + ' and ' + sorted_errors[-1]
        return f'form errors {str_errors}: {new_dance_values}'


while True:
    try:
        dance_values = input()
        print(has_error())
    except Exception:
        break

# not has_twirl, not has_hop 조건 삭제
def has_error():
    def error_test():
        nonlocal errors
        dance_list = dance_values.split()
        N = len(dance_list)
        has_twirl = has_hop = has_dip = False

        for i in range(N):
            dance_value = dance_list[i]
            if dance_value == 'dip':
                has_dip = True
                if i + 1 < N and dance_list[i + 1] == 'twirl':
                    has_twirl = True
                else:
                    for di in range(-1, -3, -1):
                        ni = i + di
                        if ni >= 0 and dance_list[ni] == 'jiggle':
                            break
                    else:
                        errors.add('1')
                        dance_list[i] = dance_value.upper()
            elif dance_value == 'twirl':
                has_twirl = True
            elif dance_value == 'hop':
                has_hop = True

        if not dance_values.endswith('clap stomp clap'):
            errors.add('2')
        if has_twirl and not has_hop:
            errors.add('3')
        if dance_list[0] == 'jiggle':
            errors.add('4')
        if not has_dip:
            errors.add('5')
        return ' '.join(dance_list)

    errors = set()
    new_dance_values = error_test()
    length = len(errors)
    if length == 0:
        return f'form ok: {new_dance_values}'
    elif length == 1:
        return f'form error {errors.pop()}: {new_dance_values}'
    else:
        sorted_errors = sorted(errors)
        str_errors = ', '.join(sorted_errors[:-1]) + ' and ' + sorted_errors[-1]
        return f'form errors {str_errors}: {new_dance_values}'

while True:
    try:
        dance_values = input()
        print(has_error())
    except Exception:
        break