def solve(games_file):
    result = 0
    with open(games_file) as f:
        for row in f:
            max_r, max_g, max_b = 0, 0, 0
            game = [subgame.split(',') for subgame in row.split(':')[1].split(';')]
            for subgame in game:
                for pick in subgame:
                    value, color = pick.strip().split(' ')
                    value = int(value)
                    if color == "red":
                        max_r = max(max_r, value)
                    elif color == "green":
                        max_g = max(max_g, value)
                    elif color == "blue":
                        max_b = max(max_b, value)
            result += max_r * max_g * max_b
    return result


print(solve("input.txt"))
