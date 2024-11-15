from collections import Counter

with open('input') as input:
    passphrases = input.read().splitlines()

passphrases = [passphrase.split(' ') for passphrase in passphrases]

def simple_valid(input):
    return max(Counter(input).values()) <= 1

def complex_valid(input):
    input = map(frozenset, input)
    return max(Counter(input).values()) <= 1

with open('output', 'w') as output:
    output.write( str(len(list(filter(simple_valid, passphrases)))) + '\n')
    output.write( str(len(list(filter(complex_valid, passphrases)))) + '\n')