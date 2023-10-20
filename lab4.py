#zadanie1
user_input = input("Enter a string with whitespaces: ")

char_list = []

for char in user_input:
    char_list.append(char.lower())

print("Created list is:")
print(char_list)

#zadanie2
user_input = input("Enter a string with whitespaces: ")

char_list = []

for char in user_input:
    char_list.append(char.lower())

print("Created list is:")
print(char_list)

char_frequency = {}

# Count the frequency of each symbol in the list
for char in char_list:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency_list = [(char, count) for char, count in char_frequency.items()]

char_frequency_list.sort()

print(char_frequency_list)

#zadanie3
user_input = input("Enter a string with whitespaces: ")

char_list = []

for char in user_input:
    char_list.append(char.lower())

print("Created list is:")
print(char_list)

char_frequency = {}

# Count the frequency of each symbol in the list
for char in char_list:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency_list = [(char, count) for char, count in char_frequency.items()]

char_frequency_list.sort()

print(char_frequency_list)

# Initialize empty lists for vowels, consonants, and symbols
list_vow = []
list_cons = []
list_sym = []

# Define a function to check if a character is a vowel
def is_vowel(char):
    vowels = 'aeiouAEIOU'
    return char in vowels

# Iterate through the input list and categorize characters
for char, count in char_frequency_list:
    if is_vowel(char):
        list_vow.append((char, count))
    elif char.isalpha():
        list_cons.append((char, count))
    else:
        list_sym.append((char, count))

# Print the categorized lists
print("list_vow =", list_vow)
print("list_cons =", list_cons)
print("list_sym =", list_sym)

#zadanie4
def divide_into_quartiles(list_A):

    list_A.sort()
    
    n = len(list_A)
    q1_index = n // 4
    q2_index = q1_index * 2
    q3_index = q1_index * 3

   
    q1 = list_A[:q1_index] + [0] * (n % 4)  
    q2 = list_A[q1_index:q2_index]
    q3 = list_A[q2_index:q3_index]
    q4 = list_A[q3_index:]

    return q1, q2, q3, q4


list_A1 = [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4]
q1, q2, q3, q4 = divide_into_quartiles(list_A1)
print("q1 =", q1)
print("q2 =", q2)
print("q3 =", q3)
print("q4 =", q4)

list_A2 = [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4, 8]
q1, q2, q3, q4 = divide_into_quartiles(list_A2)
print("q1 =", q1)
print("q2 =", q2)
print("q3 =", q3)
print("q4 =", q4)

#zadanie5
dictionary = dict();

name = input('name: ')
assignments = input('assignments: ').split(' ');
labs = input('labs: ').split(' ');
tests = input('tests: ').split(' ');

dictionary.update({'name': name, 'assignments': assignments, 'labs': labs, 'tests': tests})

print(dictionary)

#zadanie6
dictionary = dict();

name = input('name: ')
assignments = input('assignments: ').split(' ');
labs = input('labs: ').split(' ');
tests = input('tests: ').split(' ');

dictionary.update({'name': name, 'assignments': assignments, 'labs': labs, 'tests': tests})

activityDictionary = dict({dictionary.get('name'): len(dictionary.get('assignments')) + len(dictionary.get('labs')) + len(dictionary.get('tests'))})

print(activityDictionary)

#zadanie7
dictionary = dict();

name = input('name: ')
assignments = list(map(int, input('assignments: ').split(' ')));
labs = list(map(int, input('labs: ').split(' ')));
tests = list(map(int, input('tests: ').split(' ')));

print(assignments)

dictionary.update({'name': name, 'assignments': assignments, 'labs': labs, 'tests': tests})

final =  0.3 * (sum(dictionary.get('assignments')) / len(dictionary.get('assignments'))) + 0.5 * (sum(dictionary.get('labs')) / len(dictionary.get('labs'))) + 0.2 * (sum(dictionary.get('tests')) / len(dictionary.get('tests')))

if(len(dictionary.get('assignments')) > 4):
	dictionary.update({'final_grade': final})
else:
	dictionary.update({'final_grade': 0})

print(dictionary)

#zadanie8
students = dict()

studentsCount = int(input('students count: '))

for i in range(studentsCount):
	student = dict();

	name = input('name: ')
	assignments = list(map(int, input('assignments: ').split(' ')));
	labs = list(map(int, input('labs: ').split(' ')));
	tests = list(map(int, input('tests: ').split(' ')));

	student.update({'name': name, 'assignments': assignments, 'labs': labs, 'tests': tests})

	final =  0.3 * (sum(student.get('assignments')) / len(student.get('assignments'))) + 0.5 * (sum(student.get('labs')) / len(student.get('labs'))) + 0.2 * (sum(student.get('tests')) / len(student.get('tests')))

	if(len(student.get('assignments')) > 4):
		student.update({'final_grade': final})
	else:
		student.update({'final_grade': 0})
	students.update({student.get('name'): student})

print(students)

#zadanie9
stats = {}

while True:
    user_id = input("Enter user ID (or 'exit' to quit): ")
    
    if user_id.lower() == 'exit':
        break
    
    transaction_type = int(input("Enter transaction type (1 - comment, 2 - like, 3 - share): "))
    
    if user_id not in stats:
        stats[user_id] = {1: 0, 2: 0, 3: 0, 'mft': None, 'lft': None}

    stats[user_id][transaction_type] += 1

    if (
        stats[user_id]['mft'] is None
        or stats[user_id][transaction_type] > stats[user_id][stats[user_id]['mft']]
    ):
        stats[user_id]['mft'] = transaction_type
    if (
        stats[user_id]['lft'] is None
        or stats[user_id][transaction_type] < stats[user_id][stats[user_id]['lft']]
    ):
        stats[user_id]['lft'] = transaction_type

print("Statistics:")
for user_id, user_data in stats.items():
    print(f"User {user_id}: {user_data}")
