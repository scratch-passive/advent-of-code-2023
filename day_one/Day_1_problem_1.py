# The newly-improved calibration document consists of lines of text; 
# each line originally contained a specific calibration value that the Elves now need to recover. 
# On each line, the calibration value can be found by combining the first 
# digit and the last digit (in that order) to form a single two-digit number.

def main():
    sumCalibration = 0
    with open(r"C:\Users\dayna\advent-of-code-2023\day_one\advent_input.txt", "r") as file:
        for line in file:
            num1 = findFirstDigit(line)
            num2 = findLastDigit(line)
            calibrationValue = combineDigits(num1, num2)
            sumCalibration += calibrationValue
            print(line, num1, num2, calibrationValue)
    print(sumCalibration)
    return

def findFirstDigit(aString):
    for i in aString:
        if i.isdigit():
            return i

def findLastDigit(aString):
    for i in range(-1, (len(aString) +1) * -1, -1):
        if aString[i].isdigit():
            return aString[i]

def combineDigits(num1, num2):
    if num1.isdigit() and num2.isdigit():
        new = num1 + num2
        return int(new)
    else:
        return 0

main()