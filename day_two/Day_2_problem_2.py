# December 2, 2023
# Advent of Code 2023
# Day 2
# McKenzy Ison



def main(file_path: str):
    total_sum = 0              
    with open(file_path, "r") as file:
        for line in file:                   
            total_sum += get_game_power(line)
            print(total_sum)
    return


def get_game_power(a_string: str):
    max_cubes = {"red": 1, "green": 1, "blue": 1}               # Non-zero cube numbers by colour (avoids the multiply by 0)                                           
    sets = a_string[a_string.index(':')+2:].split(';')          # Trim the line into sets
    for set in sets:   
        set = (set.strip()).split(', ')
        for cube in set:
            cube = cube.split()
            if int(cube[0]) > max_cubes[cube[1]]:
                max_cubes[cube[1]] = int(cube[0])
    game_power = (max_cubes['red'] * max_cubes['green'] * max_cubes['blue'])       
    return game_power

    

def get_game_number(a_string: str):
    return ''.join(char for char in a_string[:a_string.index(':')] if char.isdigit())


file_path = r"C:\Users\dayna\advent-of-code-2023\advent-of-code-2023\day_two\advent_input.txt"

main(file_path)

'1'=='10'