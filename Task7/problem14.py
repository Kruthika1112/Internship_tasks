# 14
# Anagram
# https://www.hackerrank.com/challenges/anagram/problem


from collections import Counter

def anagram(s):
    n = len(s)

    if n % 2 != 0:
        return -1

    s1 = s[:n // 2]
    s2 = s[n // 2:]

    count1 = Counter(s1)
    count2 = Counter(s2)

    changes = 0

    for ch in count1:
        if count1[ch] > count2[ch]:
            changes += count1[ch] - count2[ch]

    return changes
