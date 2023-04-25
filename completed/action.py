def find_pattern(line):
    pattern = ''
    for i in range(1, len(line)):
        if line[:i] == line[i:2 * i]:
            pattern = line[:i]
            nested_pattern = find_pattern(line[i:])
            if nested_pattern != '':
                return nested_pattern
            break
    return pattern


def modify_paragraph(paragraph):
    modified_lines = []
    for line in paragraph.split('\n'):
        if not line:
            continue
        confirm = input(f"Do want to edit this line: \n'{line}'\n(y/n) or press Enter to skip: ")
        if len(confirm) == 0 or confirm.lower() == "n":
            modified_lines.append(line)
            continue
        extra_use = line
        pattern = find_pattern(line)
        if pattern:
            while line.startswith(pattern):
                line = line[len(pattern):]
            repeating_unit = pattern
            print(f"Repeating Unit : {repeating_unit}")
            # Prompt user to enter word
            word = input("Enter a word: ")
            # Determine the index of the target word
            words = repeating_unit.split()
            if word in words:
                word_index = words.index(word)
            else:
                print("Word not found in repeating unit.")
                continue
            # Get the adjacent words
            left_word_index = word_index - 1
            right_word_index = word_index + 1
            if left_word_index < 0:
                left_word_index = len(words) - 1
            if right_word_index >= len(words):
                right_word_index = 0
            left_word = words[left_word_index]
            right_word = words[right_word_index]
            extraCharacter = input(f"Enter a character to add infront of {right_word} : ")
            # Modify the adjacent words
            if left_word == word:
                line = line[:-1]
            else:
                left_word = left_word[:-1]
            right_word = extraCharacter + right_word
            # Construct the new repeating unit
            words[word_index] = word
            words[left_word_index] = left_word
            words[right_word_index] = right_word
            new_repeating_unit = " ".join(words) + " "

            # Prompt user to enter the occurrence number
            getOccurrence = extra_use.split()
            count = getOccurrence.count(word)
            print("The chosen word appears", count, "times in the line.")
            occurrence_num = int(input("Please choose an occurrence number (1-" + str(count) + "): "))
            if occurrence_num <= 0:
                print("Invalid occurrence number.")
                continue

            # Construct the modified line
            repeating_unit_count = occurrence_num
            line_length = len(extra_use)
            # Repeat the pattern `occurrence_num` times
            modified_line = repeating_unit * repeating_unit_count
            print(modified_line)
            # Delete the last character from the line if the word is present in the left of the repeating unit
            wordsDef = modified_line.split()
            patternCheck = pattern.split()
            if patternCheck.index(word) == 0:
                wordsDef[-1] = wordsDef[-1][:-1]
            elif patternCheck[-1] == word:
                wordsDef[-2] = wordsDef[-2][:-1]
            modified_line = " ".join(wordsDef) + " " if modified_line.endswith(" ") else " ".join(wordsDef)
            # Append the new repeating unit endlessly until the total character count equals the `extra_use` count
            while len(modified_line) < line_length:
                modified_line += new_repeating_unit
                if len(modified_line) > line_length:
                    excess_chars = len(modified_line) - line_length
                    modified_line = modified_line[:-excess_chars]
            modified_lines.append(modified_line)
        else:
            modified_lines.append(line)
    return "\n".join(modified_lines)
