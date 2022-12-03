import string

with open("input.txt", "r") as f:
    input_data = [line.strip() for line in f]

# Part 1
sacks = [set(word[:int(len(word)/2)]) & set(word[-int(len(word)/2):]) for word in input_data]
priority_numbers = dict(zip(list(string.ascii_lowercase) + list(string.ascii_uppercase), range(1, 53)))
print(sum([priority_numbers[item] for sack in sacks for item in sack]))

# Part 2
tri_matches = [set.intersection(*[set(word) for word in input_data[x:x+3]]) for x in range(0, len(input_data), 3)]
print(sum([priority_numbers[item] for match in tri_matches for item in match]))