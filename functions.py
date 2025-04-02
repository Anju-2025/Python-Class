# def calculator(num1, num2, operator):
#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#     elif operator == '*':
#         return num1 * num2
#     elif operator == '/':
#         return num1 / num2 if num2 != 0 else 'Division by zero error'
#     else:
#         return 'Invalid operator'
    
# print(calculator(50, 20, '+'))
# print(calculator(50, 20, '-'))
# print(calculator(50, 20, '*'))
# print(calculator(50, 20, '/'))


# def fibonacci(n):
#     sequence = [0, 1]
#     while len(sequence) < n:
#         sequence.append(sequence[-1] + sequence[-2])
#     return sequence[:n]


# print(fibonacci(10))


# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9

# print(celsius_to_fahrenheit(90))
# print(fahrenheit_to_celsius(100))


# def get_palindromes(numbers):
#     palindromes = []
#     for num in numbers:
        
#         if str(num) == str(num)[::-1]:
#             palindromes.append(num)
#     return palindromes


# s = [1220, 144, 1221, 2332, 4390, 9889]
# result = get_palindromes(s)
# print("Palindrome numbers:", result)


# s = [1220, 144, 1221, 2332, 4390, 9889]
# palindromes = []

# for num in s:
#     if str(num) == str(num)[::-1]:
#         palindromes.append(num)

# print("Palindrome numbers:", palindromes)


