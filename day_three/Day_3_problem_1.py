# December 3, 2023
# Advent of Code 2023
# Day 3
# McKenzy Ison
# 527364 

def main(file_path: str):
    total = 0 
    number = ''
    prev_line_symbols = set(())
    current_line_symbols = set(())
    next_line_symbols = set(())
    number_index = set(())
    with open(file_path, "r") as file:
        grid = (file.read()).split()
        
        for i in range(len(grid)):          # for each line
            
            # next line symbol index storage
            if i < len(grid) - 1:
                for j in range(len(grid[i + 1])):       # for each character in the next line
                    if not grid[i + 1][j].isnumeric() and grid[i + 1][j] != '.':
                        next_line_symbols.add(j)
                        next_line_symbols.add(j - 1)    # to account for left diagonal adjacency
                        next_line_symbols.add(j + 1)    # to account for right diagonal adjacency

            for k in range(len(grid[i])):               # for each character in the current line                
                # if the character is a symbol
                if not grid[i][k].isnumeric() and grid[i][k] != '.':
                    # store the character's index in the current
                    current_line_symbols.add(k)
                    current_line_symbols.add(k - 1)
                    current_line_symbols.add(k + 1)
                
                if grid[i][k].isnumeric():                # if the character is a digit
                    # get the whole number and all of its corresponding indexes
                    number += grid[i][k]
                    number_index.add(k)

                if not grid[i][k].isnumeric() and number != '':  # if the character is a '.'
                    # check index for number against symbol index for 
                    # previous, current, next
                    if  number_index.intersection(prev_line_symbols):                        
                        total += int(number)
                        number = ''
                        number_index.clear()
                    elif number_index.intersection(current_line_symbols):
                        total += int(number)
                        number = ''
                        number_index.clear()
                    elif number_index.intersection(next_line_symbols):
                        total += int(number)
                        number = ''
                        number_index.clear()
                    else:
                        number = ''
                        number_index.clear()
            if number != '':
                if  number_index.intersection(prev_line_symbols):                    
                    total += int(number)
                    number = ''
                    number_index.clear()
                elif number_index.intersection(current_line_symbols):                    
                    total += int(number)
                    number = ''
                    number_index.clear()
                elif number_index.intersection(next_line_symbols):                    
                    total += int(number)
                    number = ''
                    number_index.clear()
                else:
                    number = ''
                    number_index.clear()
            prev_line_symbols.clear() 
            for symbol_index in current_line_symbols:
                prev_line_symbols.add(symbol_index)           
            current_line_symbols.clear()    
            next_line_symbols.clear()
    print(total)     
                    


file_path = r"C:\Users\dayna\advent-of-code-2023\advent-of-code-2023\day_three\advent_input.txt"
main(file_path)
