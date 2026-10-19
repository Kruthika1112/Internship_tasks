# 7
# Alphabet Rangoli
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    # your code goes here
      import string
      alphabet = string.ascii_lowercase

      lines = []

      for i in range(size):
        left = alphabet[size - 1:size - i - 1:-1]
        right = alphabet[size - i - 1:size]
        row = left + right
        pattern = "-".join(row)
        lines.append(pattern.center(4 * size - 3, "-"))

      for i in range(size - 2, -1, -1):
        left = alphabet[size - 1:size - i - 1:-1]
        right = alphabet[size - i - 1:size]
        row = left + right
        pattern = "-".join(row)
        lines.append(pattern.center(4 * size - 3, "-"))

      print("\n".join(lines))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)