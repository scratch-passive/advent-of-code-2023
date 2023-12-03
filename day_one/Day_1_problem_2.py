# December 1, 2023
# Advent of Code 2023
# Day 1
# McKenzy Ison


def main(file_path):
    sum_calibration = 0
    digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
              '9': '9', '8': '8', '7':'7', '6':'6', '5':'5', '4': '4', '3':'3', '2':'2', '1':'1'}
    
    with open(file_path, "r") as file:
        

        for line in file:
            
            i_digits = {}
            for key in digits:
                if key in line:
                    i_digits[line.index(key)] = digits[key]
                    i_digits[line.rindex(key)] = digits[key]
            
            print(i_digits, line)
            calibration_value = int(i_digits[min(i_digits)] + i_digits[max(i_digits)]) 
            sum_calibration += calibration_value
            
            
    
    print(sum_calibration)
    return

file_path = r"C:\Users\dayna\advent-of-code-2023\advent-of-code-2023\day_one\advent_input.txt"
main(file_path)