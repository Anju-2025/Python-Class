# # Given list
# a = [20, "python", 30.5, False]

# # Empty lists to store elements by type
# integers = []
# strings = []
# booleans = []
# floats = []

# # Loop through each element and check its type
# for element in a:
#     if isinstance(element, bool):  # Check for boolean first
#         booleans.append(element)
#     elif isinstance(element, int):  # Then check for integers
#         integers.append(element)
#     elif isinstance(element, str):
#         strings.append(element)
#     elif isinstance(element, float):
#         floats.append(element)

# # Display the lists based on type
# print("Integers:", integers)
# print("Strings:", strings)
# print("Booleans:", booleans)
# print("Floats:", floats)


# check a string is palindrome or not

# input_string = input("Enter a string: ")

# normalized_string = input_string.replace(" ", "").lower()

# if normalized_string == normalized_string[::-1]:
#     print(f"'{input_string}' is a palindrome.")
# else:
#     print(f"'{input_string}' is not a palindrome.")

# # reverse of a string using while loop
# # Get input from the user
# number = int(input("Enter a number: "))

# Initialize variables
# number=201
# reverse = 0

# # While loop to reverse the digits of the number
# while number > 0:
#     remainder = number % 10
#     reverse = reverse * 10 + remainder
#     number //= 10

# print(f"The reversed number is: {reverse}")


# reverse of a string using while loop

# input_string = input("Enter a string: ")

# reversed_string = ""

# index = len(input_string) - 1

# while index >= 0:
#     reversed_string += input_string[index]
#     index -= 1  

# print("Reversed string:", reversed_string)


# import random

# primes_in_range = []

# for num in range(100, 120):
#     is_prime = True
#     for i in range(2, num):
#         if num % i== 0:
#             is_prime = False
#             break
#     if is_prime:
#             primes_in_range.append(num)
# print(primes_in_range)
# random_primes = random.sample(primes_in_range, 3)
# print(random_primes)


# Example lists
# keys = ['name', 'age', 'city']
# values = ['Alice', 25, 'New York']

# # Initialize an empty dictionary
# result = {}

# # Use a for loop to populate the dictionary
# for i in range(len(keys)):
#     result[keys[i]] = values[i]

# print(result)



def show(words):
    k = []  
    vowels = ["a", "e", "i", "o", "u"]

    for word in words:
        for char in word:
            if char in vowels:
                k.append(word)
                break 
    print(k)
a = ["fly", "apple", "sky", "education", "spy", "kite", "rhythm", 'rain']
show(a)

# Write a function extract_words_with_letter(words, letter) that takes a list of words and a specific letter. 
# It should return a list of words that contain that letter at least once.

def extract_words_with_letter(words, letter):
    result = []
    for word in words:
        if letter in word:
            result.append(word)
    return result

words = ["banana", "apple", "grape", "mango", "kiwi"]
print(extract_words_with_letter(words, "a"))


# Write a function words_starting_with_vowel(words) 
# that takes a list of words and returns a list of words that start with a vowel.

def words_starting_with_vowel(words):
    vowels = "aeiou"
    result = []
    for word in words:
        if word[0].lower() in vowels:
            result.append(word)
    return result

words = ["apple", "banana", "orange", "umbrella", "grape", "elephant"]
print(words_starting_with_vowel(words))


# Write a function count_vowels_in_words(words) that takes a list of words and returns a dictionary 
# where each word is a key, and its value is the number of vowels in that word.

def count_vowels_in_words(words):
    vowels = "aeiou"
    result = {}
    for word in words:
        count = 0
        for char in word:
            if char in vowels:
                count += 1
        result[word] = count
    return result

words = ["apple", "banana", "grape"]
print(count_vowels_in_words(words))


# Write a function filter_words_by_length(words, length) that takes a list of words and an integer length. 
# It should return a list of words with length greater than or equal to the specified length.


def filter_words_by_length(words, length):
    result = []
    for word in words:
        if len(word) >= length:
            result.append(word)
    return result

words = ["apple", "banana", "grape", "kiwi"]
print(filter_words_by_length(words, 5))


# Write a function separate_even_odd_length_words(words) that takes a list of words and 
# returns two lists: one containing words with an even length and another with words with an odd length.

def separate_even_odd_length_words(words):
    even_length_words = []
    odd_length_words = []
    for word in words:
        if len(word) % 2 == 0:
            even_length_words.append(word)
        else:
            odd_length_words.append(word)
    return even_length_words, odd_length_words

words = ["apple", "banana", "grape", "kiwi", "pear"]
print(separate_even_odd_length_words(words))


