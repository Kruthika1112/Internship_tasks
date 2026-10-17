# 20
# Piling Up!
# https://www.hackerrank.com/challenges/piling-up/problem


t = int(input())

for _ in range(t):
    n = int(input())
    blocks = list(map(int, input().split()))

    left = 0
    right = n - 1
    top = float('inf')
    possible = True

    while left <= right:
        if blocks[left] >= blocks[right]:
            current = blocks[left]
            left += 1
        else:
            current = blocks[right]
            right -= 1

        if current > top:
            possible = False
            break

        top = current

    print("Yes" if possible else "No")
