#230630
#
A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

print(min(A*P, B if P <= C else B+D*(P-C)))

#
A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

cost_x = A*P
cost_y = B if P <= C else B+D*(P-C)
print(min(cost_x, cost_y))

#
A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

cost_x = A*P
cost_y = B
if P > C:
    cost_y += D*(P-C)
print(min(cost_x, cost_y))

#
def min_cost():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    P = int(input())

    cost_x = A*P
    cost_y = B if P <= C else B+D*(P-C)
    return min(cost_x, cost_y)

print(min_cost())