with open('input') as input:
    instructions = input.read().splitlines()
instructions = list(map(int, instructions))

def jump_maze(maze, f):
    steps = 0
    index = 0
    while 0 <= index < len(maze):
        jump_value = maze[index]
        maze[index] = f(maze[index])
        index += jump_value
        steps += 1
    return steps

with open('output', 'w') as output:
    output.write( str(jump_maze(instructions.copy(), lambda x: x + 1)) + '\n')
    output.write( str(jump_maze(instructions.copy(), lambda x: x - 1 if x >= 3 else x + 1)) + '\n')