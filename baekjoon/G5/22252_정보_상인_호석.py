# 260205
# 38580 KB / 3224 ms
def main():
    from heapq import heappop, heapify

    Q = int(input())
    name_to_info = {}
    total = 0

    def minus_int(num):
        return -int(num)

    for _ in range(Q):
        type_of, name, k, *info = input().split()
        if type_of == '1':
            if not name_to_info.get(name):
                name_to_info[name] = []

            name_to_info[name].extend(list(map(minus_int, info)))
            heapify(name_to_info[name])

        elif name_to_info.get(name):
            for _ in range(int(k)):
                max_val = heappop(name_to_info[name])
                total -= max_val
                if not name_to_info[name]:
                    break

    return total

print(main())





# 36504 KB / 3000 ms
def main():

    Q = int(input())
    name_to_info = {}
    total = 0

    for _ in range(Q):
        type_of, name, k, *info = input().split()
        if type_of == '1':
            if not name_to_info.get(name):
                name_to_info[name] = []

            name_to_info[name].extend(list(map(int, info)))

        elif name_to_info.get(name):
            name_to_info[name].sort()
            for _ in range(int(k)):
                total += name_to_info[name].pop()
                if not name_to_info[name]:
                    break

    return total

print(main())







#  36504 KB / 3076 ms
def main():

    Q = int(input())
    name_to_info = {}
    total = 0

    for _ in range(Q):
        type_of, name, k, *info = input().split()
        if type_of == '1':
            if not name_to_info.get(name):
                name_to_info[name] = []

            name_to_info[name].extend(list(map(int, info)))

        elif name_to_info.get(name):
            name_to_info[name].sort()
            i = 0
            while i < int(k) and name_to_info[name]:
                total += name_to_info[name].pop()
                i += 1

    return total

print(main())








#  36504 KB / 2804 ms
def main():

    Q = int(input())
    name_to_info = {}
    total = 0

    for _ in range(Q):
        type_of, name, k, *info = input().split()
        if type_of == '1':
            if not name_to_info.get(name):
                name_to_info[name] = []

            name_to_info[name].extend(list(map(int, info)))

        elif name_to_info.get(name):
            if int(k) < len(name_to_info[name]):
                name_to_info[name].sort()
                i = 0
                while i < int(k) and name_to_info[name]:
                    total += name_to_info[name].pop()
                    i += 1
            else:
                total += sum(name_to_info[name])
                name_to_info[name] = []

    return total

print(main())





# 36504 KB / 360 ms
def main():
    from sys import stdin

    new_input = stdin.readline

    Q = int(new_input())
    name_to_info = {}
    total = 0

    for _ in range(Q):
        type_of, name, k, *info = new_input().split()
        if type_of == '1':
            if not name_to_info.get(name):
                name_to_info[name] = []

            name_to_info[name].extend(list(map(int, info)))

        elif name_to_info.get(name):
            if int(k) < len(name_to_info[name]):
                name_to_info[name].sort()
                i = 0
                while i < int(k) and name_to_info[name]:
                    total += name_to_info[name].pop()
                    i += 1
            else:
                total += sum(name_to_info[name])
                name_to_info[name] = []

    return total

print(main())