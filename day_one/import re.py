import re

def extract_digits(line, spelled_out=False):
    # Use regular expression to find digits (either numerical or spelled out)
    pattern = r'\d+|[a-zA-Z]+'
    digits = re.findall(pattern, line)

    # Convert spelled-out digits to numerical
    if spelled_out:
        digit_mapping = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
        digits = [digit_mapping.get(d, d) for d in digits]

    return digits

def calculate_calibration_sum(lines, spelled_out=False):
    total_sum = 0
    for line in lines:
        digits = extract_digits(line, spelled_out)
        if digits:
            total_sum += int(digits[0] + digits[-1])

    return total_sum

# Example usage:
calibration_document = open(r"C:\Users\dayna\advent-of-code-2023\advent-of-code-2023\day_one\advent_input.txt", "r")

# = [
#     "two1nine",
#     "eightwothree",
#     "abcone2threexyz",
#     "xtwone3four",
#     "4nineeightseven2",
#     "zoneight234",
#     "7pqrstsixteen"
# ]

# Part One
sum_part_one = calculate_calibration_sum(calibration_document)
print(f"Part One: Sum of calibration values: {sum_part_one}")

# Part Two
sum_part_two = calculate_calibration_sum(calibration_document, spelled_out=True)
print(f"Part Two: Sum of calibration values with spelled-out digits: {sum_part_two}")
