# 16
# Collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem


from collections import Counter

X = int(input())
shoe_sizes = list(map(int, input().split()))

shoe_count = Counter(shoe_sizes)

N = int(input())
earnings = 0

for _ in range(N):
    size, price = map(int, input().split())

    if shoe_count[size] > 0:
        earnings += price
        shoe_count[size] -= 1

print(earnings)
