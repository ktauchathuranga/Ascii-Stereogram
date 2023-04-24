repeating_unit = "mama lol my hand car "
total_length = 100

# Prompt user to enter word and direction
word = input("Enter a word: ")
direction = input("Enter 'left' or 'right': ")

# Determine the index of the target word
words = repeating_unit.strip().split()
if word in words:
    word_index = words.index(word)
    if direction == "right":
        word_index += 1
    else:
        word_index -= 1
else:
    print("Word not found in repeating unit.")
    exit()

# Get the adjacent word based on the direction
if word_index < 0:
    adjacent_word = words[-1]
elif word_index >= len(words):
    adjacent_word = words[0]
else:
    adjacent_word = words[word_index]

print(adjacent_word)
