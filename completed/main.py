import action
from datetime import datetime


def generate_repeating_pattern(lines, chars_per_line):
    """
    Generates a block of a repeating pattern paragraph based on user inputs.

    Args:
        lines (int): The number of lines in the block.
        chars_per_line (int): The total number of characters (including spaces) in one line.

    Returns:
        str: The generated repeating pattern paragraph.
    """
    repeating_pattern = ""
    for i in range(lines):
        text = input("Enter the text for line {}: ".format(i + 1))
        pattern = ""
        while len(pattern) < chars_per_line:
            pattern += text + " "
        pattern = pattern[:chars_per_line]
        repeating_pattern += pattern + "\n"
    return repeating_pattern


# Get user inputs for the number of lines and characters per line
lines = int(input("Enter the number of lines in the block: "))
chars_per_line = int(input("Enter the total number of characters (including spaces) in one line: "))

# Generate the repeating pattern paragraph
repeating_pattern_paragraph = generate_repeating_pattern(lines, chars_per_line)

# Print the repeating pattern paragraph
print(repeating_pattern_paragraph)

modifiedParagraph = action.modify_paragraph(repeating_pattern_paragraph)

print(modifiedParagraph)

current_date_time = datetime.now()
file_name = f"stereogram - {current_date_time.strftime('%Y-%m-%d %H-%M-%S')}.txt"
with open(file_name, 'w') as file:
    file.write(modifiedParagraph)
