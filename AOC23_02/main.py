#12 red cubes, 13 green cubes, and 14 blue cubes
cond = {"r":12, "g":13, "b":14}
result = 0

with open("input.txt") as file:
    for row in file:
        possible = True
        game, cubes = row.split(':')
        cube_picks = cubes.split(';')
        for cp in cube_picks:
            cube_pick = cp.split(',')
            for cube in cube_pick:
                num, color = cube.strip().split(" ")
                num = int(num)
                if color == "red" and 12 < num:
                    possible = False
                elif color == "green" and 13 < num:
                    possible = False
                elif color == "blue" and 14 < num:
                    possible = False
            if not possible:
                break
        if possible:
            #print(int(game.split(" ")[1]))
            result += int(game.split(" ")[1])
print(result)
