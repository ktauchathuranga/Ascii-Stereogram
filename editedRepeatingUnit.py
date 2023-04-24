repeating_unit = "lol my hand "
total_length = 100

# Prompt user to enter word
word = input("Enter a word: ")

# Determine the index of the target word
words = repeating_unit.strip().split()
if word in words:
    word_index = words.index(word)
else:
    print("Word not found in repeating unit.")
    exit()

# Get the adjacent words
left_word_index = word_index - 1
right_word_index = word_index + 1
if left_word_index < 0:
    left_word_index = len(words) - 1
if right_word_index >= len(words):
    right_word_index = 0
left_word = words[left_word_index]
right_word = words[right_word_index]

# Modify the adjacent words
left_word = left_word[:-1]
right_word = "A" + right_word

# Construct the new repeating unit
words[word_index] = word
words[left_word_index] = left_word
words[right_word_index] = right_word
new_repeating_unit = " ".join(words) + " "

print(new_repeating_unit)
