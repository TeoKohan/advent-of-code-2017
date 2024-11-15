import re

with open('input') as input:
    memory_banks = input.readline()
memory_banks = list(map(int, re.findall(r'\d+', memory_banks)))

def execute_reallocation_non_repeating(memory_banks: list[int]):

    def reallocate(memory_banks):
        index = memory_banks.index(max(memory_banks))
        blocks = memory_banks[index]
        memory_banks[index] = 0

        for i in range(1, blocks+1):
            memory_banks[(index+i)%len(memory_banks)] += 1
    
    cycles = 0
    seen_memory_banks = dict()

    while not tuple(memory_banks) in seen_memory_banks:
        seen_memory_banks[tuple(memory_banks)] = cycles
        reallocate(memory_banks)
        cycles += 1

    return cycles, cycles - seen_memory_banks[tuple(memory_banks)]

with open('output', 'w') as output:
    cycles, loop_length = execute_reallocation_non_repeating(memory_banks.copy())
    output.write(str(cycles) + '\n')
    output.write(str(loop_length) + '\n')
