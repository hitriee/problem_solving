#230415
T = int(input())
other_set = set()
for _ in range(T):
    sound_list = input().split()
    while True:
        info = input().split()
        if len(info) > 3:
            break
        other_set.add(info[-1])
    sound_of_fox = ''
    for sound in sound_list:
        if sound not in other_set:
            sound_of_fox += f'{sound} '
    print(sound_of_fox.rstrip())
    other_set.clear()
