def find_pattern(line):
    pattern = ''
    for i in range(1, len(line)):
        if line[:i] == line[i:2*i]:
            pattern = line[:i]
            nested_pattern = find_pattern(line[i:])
            if nested_pattern != '':
                return nested_pattern
            break
    return pattern

line = input("Enter a line of text: ")
pattern = find_pattern(line)
if pattern:
    while line.startswith(pattern):
        line = line[len(pattern):]
    print(pattern)
else:
    print("No pattern found.")