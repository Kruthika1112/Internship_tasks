
# Q1. Find the Frequency of Each Word in a Sentence

from solutions import frequency
sentence = "python is easy and python is powerful"
print("Given example:", frequency(sentence))
# Additional test case
sentence2 = "hello world hello"
print("Additional test:", frequency(sentence2))


# Q2. Find the Frequency of Each Character in a Word

from solutions import char_frequency
word = "banana"
print("Given example:",char_frequency(word))
# Additional test case
word2 = "hello"
print("Additional test:", char_frequency(word2))


from solutions import first_non_repeating
# Given example
word = "swiss"
print("Given example:", first_non_repeating(word))
# Additional test case
word2 = "aabb"
print("Additional test:", first_non_repeating(word2))


from solutions import are_anagrams
# Given example
s1 = "listen"
s2 = "silent"
print("Given example:", are_anagrams(s1, s2))
# Additional test case
s3 = "hello"
s4 = "world"
print("Additional test:", are_anagrams(s3, s4))


from solutions import first_repeating
# Given example
string = "programming"
print("Given example:", first_repeating(string))
# Additional test case
string2 = "abcdef"
print("Additional test:", first_repeating(string2))


from solutions import move_zeros
# Given example
nums = [0, 3, 0, 1, 2, 0, 4]
print("Given example:", move_zeros(nums))
# Additional test case
nums2 = [1, 0, 2, 0, 3]
print("Additional test:", move_zeros(nums2))


from solutions import second_highest
# Given example
nums = [10, 20, 40, 30, 40, 20]
print("Given example:", second_highest(nums))
# Additional test case
nums2 = [5, 5, 5]
print("Additional test:", second_highest(nums2))


from solutions import remove_duplicates
# Given example
nums = [4, 2, 4, 5, 2, 7, 5]
print("Given example:", remove_duplicates(nums))
# Additional test case
nums2 = [1, 1, 2, 3, 2]
print("Additional test:", remove_duplicates(nums2))


from solutions import missing_number
# Given example
nums = [1, 2, 4, 5, 6]
n = 6
print("Given example:", missing_number(nums, n))
# Additional test case
nums2 = [1, 3, 4]
n2 = 4
print("Additional test:", missing_number(nums2, n2))


from solutions import two_sum

# Given example
nums = [2, 7, 11, 15]
target = 9
print("Given example:", two_sum(nums, target))

# Additional test case
nums2 = [1, 2, 4]
target2 = 20
print("Additional test:", two_sum(nums2, target2))


from solutions import closest_to_zero
# Given example
nums = [-8, -3, 2, 5, -2]
print("Given example:", closest_to_zero(nums))

# Additional test case
nums2 = [-4, -1, 1, 3]
print("Additional test:", closest_to_zero(nums2))


from solutions import common_elements
# Given example
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print("Given example:", common_elements(list1, list2))
# Additional test case
list3 = [2, 2, 3, 4]
list4 = [4, 2]
print("Additional test:", common_elements(list3, list4))


from solutions import rotate_right
# Given example
nums = [1, 2, 3, 4, 5]
k = 2
print("Given example:", rotate_right(nums, k))
# Additional test case
nums2 = [1, 2, 3]
k2 = 4
print("Additional test:", rotate_right(nums2, k2))


from solutions import max_consecutive_sum
# Given example
nums = [4, 7, 2, 9, 5]
print("Given example:", max_consecutive_sum(nums))
# Additional test case
nums2 = [-5, -2, -8]
print("Additional test:", max_consecutive_sum(nums2))


from solutions import all_pairs

# Given example
nums = [2, 4, 3, 5, 7, 8, 1]
target = 9
print("Given example:", all_pairs(nums, target))

# Additional test case
nums2 = [1, 1, 2, 2, 3, 4]
target2 = 4
print("Additional test:", all_pairs(nums2, target2))
