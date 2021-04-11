import random
import string
import random
import csv
import sys

letter_allowlist = set(string.ascii_lowercase)
names = []

with open(sys.argv[1], encoding="utf8") as names_file:
    reader = csv.reader(names_file)

    for row in reader:
        raw_name = row[0]

        if len(raw_name) != 3:
            continue

        occurance = float(row[1])

        if occurance < 0.5:
            continue

        name = raw_name.lower()

        if len(set(name).intersection(letter_allowlist)) != 3:
            continue

        names.append(name)

alphabet = list(string.ascii_lowercase)
vowels = set('aeiouy')
first_frequency = {}

for letter in alphabet:
    first_frequency[letter] = {}

    for next_letter in alphabet:
        first_frequency[letter][next_letter] = 0.1

second_frequency = {}

for letter in alphabet:
    second_frequency[letter] = {}

    for next_letter in alphabet:
        second_frequency[letter][next_letter] = 0.1

for name in names:
    first_frequency[name[0]][name[1]] += 2
    second_frequency[name[1]][name[2]] += 2

def next_letter(letter, frequency):
    return random.choices(list(frequency[letter].keys()), frequency[letter].values())[0]

print('Generated names:')
for _ in range(0, 30):
    first_letter = random.choice(alphabet)
    second_letter = next_letter(first_letter, first_frequency)
    third_letter  = next_letter(second_letter, second_frequency)

    if len(set([first_letter, second_letter, third_letter]).intersection(vowels)) == 0:
        second_letter = random.choice(list(vowels))
    name = first_letter + second_letter + third_letter
    in_list = 1 if name in names else 0
    print(f'{name} {in_list}')
