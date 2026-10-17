# 8
# Tuples
# https://www.hackerrank.com/challenges/python-tuples/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT



if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))

    mask = (1 << 64) - 1
    x = 0x345678
    mult = 1000003

    for i, item in enumerate(t):
        y = -2 if item == -1 else item
        x = ((x ^ (y & mask)) * mult) & mask
        remaining = n - i - 1
        mult += 82520 + 2 * remaining

    x = (x + 97531) & mask

    if x >= (1 << 63):
        x -= (1 << 64)

    print(x)


