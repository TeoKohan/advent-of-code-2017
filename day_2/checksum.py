import re

with open('input') as input:
    checksum = input.readlines()
    checksum = [list(map(int, re.findall(r'\d+', line))) for line in checksum]

    minmax_values = []
    divide_values = []
    
    for line in checksum:
        minmax_values.append(max(line) - min(line))

    for line in checksum:
        divide_values += [line[i] // line[j] for i in range(len(line)) for j in range(len(line)) if i != j and line[i] % line[j] == 0]

with open('output', 'w') as output:
    output.write( str(sum(minmax_values)) + '\n')
    output.write( str(sum(divide_values)) + '\n')