class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v):
        return Vector2(self.x + v.x, self.y + v.y)
    
    def __sub__(self, v):
        return Vector2(self.x - v.x, self.y - v.y)

    def __mul__(self, s):
        return Vector2(self.x * s, self.y * s)
    
    def __rmul__(self, s):
        return self.__mul__(s)

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __iter__(self):
        yield self.x
        yield self.y

with open('input') as input:
    memory_position: int = int(input.readline())

def spiral_generator():
    length = 1
    direction = Vector2(1, 0)

    def rotate_ccw(v):
        v.x, v.y = -v.y, v.x
        
    while (True):
        yield direction, length
        rotate_ccw(direction)
        yield direction, length
        rotate_ccw(direction)
        length += 1

def calculate_memory_position(memory_position):
    spiral = spiral_generator()
    memory_steps_left = memory_position - 1
    position = Vector2(0, 0)
    while memory_steps_left > 0:
        direction, length = next(spiral)
        length = min(memory_steps_left, length)
        position += direction * length
        memory_steps_left -= length
    return abs(position.x) + abs(position.y)

def data_cap(memory_cap):
    spiral = spiral_generator()
    position = Vector2(0, 0)
    data = {Vector2(0, 0): 1}

    def close_keys(input_key, data):
        length = lambda v: max(abs(v.x), abs(v.y))
        return [key for key in data if length(key - input_key) == 1]

    def value_of(input_key, data):
        keys = close_keys(input_key, data)
        return sum([data[key] for key in keys])

    for direction, length in spiral:
        for _ in range(length):
            position += direction
            data[position] = value_of(position, data)
            if data[position] > memory_cap:
                return data[position]

with open('output', 'w') as output:
    output.write( str(calculate_memory_position(memory_position)) + '\n')
    output.write( str(data_cap(memory_position)) + '\n')