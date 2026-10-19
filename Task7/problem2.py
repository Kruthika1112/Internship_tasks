# 2
# The Captain's Room
# https://www.hackerrank.com/challenges/py-the-captains-room/problem


from collections import Counter
k = int(input())
rooms = list(map(int, input().split()))
counts = Counter(rooms)
for room, count in counts.items():
    if count == 1:
        print(room)
        break
