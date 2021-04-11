import random
import string
import random

with open('names.txt') as names_file:
    names = [name.strip().lower() for name in names_file.readlines()]

alphabet = list(string.ascii_lowercase)
frequency = {}

for letter in alphabet:
    frequency[letter] = {}

    for next_letter in alphabet:
        frequency[letter][next_letter] = 0

for name in names:
    frequency[name[0]][name[1]] += 1
    frequency[name[1]][name[2]] += 1

def next_letter(letter):
    return random.choices(list(frequency[letter].keys()), frequency[letter].values())[0]

print('Generated names:')
for _ in range(0, 30):
    first_letter = random.choice(alphabet)
    second_letter = next_letter(first_letter)
    third_letter  = next_letter(second_letter)
    print(first_letter.upper() + second_letter + third_letter)
