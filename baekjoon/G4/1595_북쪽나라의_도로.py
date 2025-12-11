# 251211
# 34456 KB / 44 ms
def main():
    from sys import stdin, setrecursionlimit

    setrecursionlimit(10000)
    new_input = stdin.readline
    cities = {}
    end_city = max_val = city = 0

    while True:
        try:
            city1, city2, gap = map(int, new_input().split())
            city = city1

            cities[city1] = cities.get(city1, []) + [(city2, gap)]
            cities[city2] = cities.get(city2, []) + [(city1, gap)]
        except:
            break

    if city == 0:
        return 0

    def find_distant_city(present_city, val):
        nonlocal end_city, max_val

        visited.add(present_city)
        for next_city, gap in cities[present_city]:
            if next_city not in visited:
                new_val = val+gap
                if max_val < new_val:
                    end_city, max_val = next_city, new_val

                find_distant_city(next_city, new_val)
        visited.remove(present_city)

    visited = set()
    find_distant_city(city, 0)

    visited = set()
    max_val = 0
    find_distant_city(end_city, 0)
    return max_val


print(main())