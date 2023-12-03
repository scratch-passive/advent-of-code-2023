# December 2, 2023
# Advent of Code 2023
# Day 2
# McKenzy Ison



def main(file_path: str):
     
    total_sum = 0              # Maximmum (red_cubes, green_cubes, blue_cubes) or (r, g, b)
    with open(file_path, "r") as file:
        for line in file:                   # Read line by line
            print(line)
            game_number = get_game_number(line)
            if is_game_valid(line):
                total_sum += int(game_number)
            print(total_sum)
    return


def is_game_valid(a_string: str):
    max_cubes = {"red": 12, "green": 13, "blue": 14}            # Limits to cube numbers by colour
    flag = True                                                 # Unless the set fails, the game passes 
    sets = a_string[a_string.index(':')+2:].split(';')          # Trim the line into sets
    for set in sets:   
                                                 # Checking each set for a false flag
        set = (set.strip()).split(', ')
        for cube in set:

            cube = cube.split()
            if max_cubes[cube[1]] < int(cube[0]): 
                              # If the cubes are greater than the maximum amounts
                flag = False
                return flag    
    return flag

    

def get_game_number(a_string: str):
    return ''.join(char for char in a_string[:a_string.index(':')] if char.isdigit())


file_path = r"C:\Users\dayna\advent-of-code-2023\advent-of-code-2023\day_two\advent_input.txt"

main(file_path)

'1'=='10'