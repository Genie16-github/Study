import sys
from math import factorial
input = sys.stdin.readline

def solve(string, i):
    global cnt
    if i == len(a):
        cnt += 1
        if cnt == b:
            return string
    else:
        for k in a:
            if k not in string:
                res = solve(string + k, i + 1)

                if res:
                    return res

    return

while True:
    cnt = 0
    data = input().split()

    if len(data) != 2:
        break

    a, b = data
    b = int(b)

    if factorial(len(a)) < b:
        print(a, b, '=', 'No permutation')
    else:
        print(a, b, '=', solve('', 0))