with open('input') as input:
    captcha = list(map(int, input.read().rstrip()))

    next_matches = []
    half_matches = []

    def repeats_ahead(captcha: list[int], index: int, skip: int) -> bool:
        return captcha[index] == captcha[(index+skip)%len(captcha)]
    
    for i in range(len(captcha)):
        if repeats_ahead(captcha, i, 1):
            next_matches.append(captcha[i])
        if repeats_ahead(captcha, i, len(captcha) // 2):
            half_matches.append(captcha[i])

with open('output', 'w') as output:
    output.write( str(sum(next_matches)) + '\n')
    output.write( str(sum(half_matches)) + '\n')