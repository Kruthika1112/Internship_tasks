
# Q1. Find the Frequency of Each Word in a Sentence

def frequency(sentence):
    words = sentence.lower().split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
        
            frequency[word] = 1

    return frequency



# Q2. Find the Frequency of Each Character in a Word

def char_frequency(word):
    frequency = {}

    for char in word:
        if char in frequency:
            frequency[char] += 1

        else:
            frequency[char] = 1

    return frequency



# Q3. Find the First Non-Repeating Character in a Word

def first_non_repeating(word):
    for char in word:
        if word.count(char) == 1:
            return char

    return None


# Q4. Check Whether Two Strings Are Anagrams
def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1.lower()) == sorted(s2.lower())


# Q5. Find the First Repeating Character in a String

def first_repeating(string):
    seen = set()
    for char in string:
        if char in seen:
            return char
        else:
            seen.add(char)
    return None


# Q6. Move All Zeros to the End of a List

def move_zeros(nums):
    result = []
    zero_count = 0
    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            result.append(num)
    result.extend([0] * zero_count)
    return result


# Q7. Find the Second Highest Distinct Number in a List

def second_highest(nums):
    unique_nums = sorted(set(nums), reverse=True)
    if len(unique_nums) < 2:
        return None
    return unique_nums[1]


# Q8. Remove Duplicates Without Changing the Original Order

def remove_duplicates(nums):
    result = []
    seen = set()
    for num in nums:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result


# Q9. Find the Missing Number from 1 to N

def missing_number(nums, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


# Q10. Find Two Numbers Whose Sum Equals a Target

def two_sum(nums, target):
    for j in range(len(nums)):
        for i in range(j):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]

    return []


# Q11. Find the Number Closest to Zero

def closest_to_zero(nums):
    if not nums:
        return None
    return min(nums, key=lambda num: (abs(num), -num))



# Q12. Find Common Elements Between Two Lists

def common_elements(list1, list2):
    result = []
    seen = set()
    for num in list1:
        if num in list2 and num not in seen:
            result.append(num)
            seen.add(num)
    return result



# Q13. Rotate a List to the Right by K Positions

def rotate_right(nums, k):
    if not nums:
        return []
    k = k % len(nums)
    return nums[-k:] + nums[:-k] if k != 0 else nums[:]


# Q14. Find the Maximum Sum of Two Consecutive Elements

def max_consecutive_sum(nums):
    maximum = nums[0] + nums[1]
    for i in range(1, len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]
        if current_sum > maximum:
            maximum = current_sum
    return maximum


# Q15. Find All Pairs of Numbers Whose Sum Equals a Target

def all_pairs(nums, target):
    pairs = set()

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = tuple(sorted([nums[i], nums[j]]))
                pairs.add(pair)

    return [list(pair) for pair in sorted(pairs)]
