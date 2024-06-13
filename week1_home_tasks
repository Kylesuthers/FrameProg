# sum of even numbers
def sum_of_numbers(list):
    result = sum(num for num in list if num % 2 == 0)
    return result
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_of_numbers(numbers))

# output = first and last charachters only
string = "Hello World"
def first_last_letters(letter):
    if len(letter) < 2:
        return letter
    else:
        return letter[0] + letter[-1]
print(first_last_letters(string))

# show common elements between 2 lists
def common_elements(list1, list2):
    result = [value for value in list1 if value in list2]
    return result

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
print(common_elements(list1, list2))

# output = numbers greater than list average
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def greater_than_average(list3):
    average = sum(list3) / len(list3)
    result = [value for value in list3 if value > average]
    print(result)

greater_than_average(list3)

# reverse string w/o user input
string_test = "Hello World"
print(string_test[::-1])

#output = positve even numbers only
list4 = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
result = [value for value in list4 if value > 0 and value % 2 == 0]
print(result)

#show times table for user input number
number_to_multiply = int(input('Enter number for which you wish to multiply   '))
for i in range(1, 11):
    print(i, "X", number_to_multiply , "=", number_to_multiply * i)

# set 2 functions

#fuction to add any given numbers
def add_numbers():
    numbers_to_add = input('Enter numbers you want to add: ')
    numbers_to_add = numbers_to_add.split()
    numbers_to_add = [int(num) for num in numbers_to_add]
    result = sum(numbers_to_add)
    print(result)

add_numbers()

# function to reverse a string
def string_to_reverse():
    user_string = input('Enter String: ')
    print (user_string[::-1])

string_to_reverse()

# function to calculate average
def averages():
    numbers = input('Enter a series of numbers: ')
    numbers = numbers.split()
    numbers = [int(num) for num in numbers]
    average = sum(numbers) / len(numbers)
    print(average)

averages()

#ount charaters
def count_char():
    user_string = input('Enter a string: ')
    char_to_count = input('Enter a character to count: ')
    count = user_string.count(char_to_count)
    print(count)

count_char()

#get even numbers

def get_even_numbers():
    numbers = input('Enter a series of numbers: ')
    numbers = numbers.split()
    numbers = [int(num) for num in numbers]
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(even_numbers)

get_even_numbers()

# find the longest string

def find_longest_word():
    words = input("Enter words you wish to find longest of: ")
    longest_word = max(words.split(), key = len)
    return longest_word
print(find_longest_word())

find_longest_word()
# product_of_numbers
def product_of_numbers():
    numbers = input("Enter numbers you wish to find product of: ")
    numbers = numbers.split()
    numbers = [int(num) for num in numbers]
    product = 1
    for num in numbers:
        product *= num
    return product
print(product_of_numbers())

product_of_numbers()


#count words in string

def count_word_occurrence():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    word_count = dict()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

print(count_word_occurrence())

count_word_occurrence()

#find strings in a list of strings
def find_strings():
    list_of_string = input("Enter the words, separated by commas: ").split(',')
    single_string = input("Enter the word to find: ")

    words_list = [word.strip() for word in list_of_string]

    return [word for word in words_list if single_string in word]
print(find_strings())

find_strings()

#find the max difference
def find_max_diff():
    numbers = input("Enter a series of numbers: ")
    numbers = numbers.split()
    numbers = [int(num) for num in numbers]
    max_diff = max(numbers) - min(numbers)
    return max_diff
print(find_max_diff())

find_max_diff()
