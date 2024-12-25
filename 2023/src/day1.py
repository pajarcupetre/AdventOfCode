#!/usr/bin/python3
import sys

def sum_calibration(lines):
    sum = 0
    for line in lines:
        digits = []
        for c in line:
            if c.isdigit():
                digits.append(c)
        if len(digits) > 0:
            sum +=  int(digits[0])*10 + int(digits[len(digits)-1])
    return sum

def sum_calibration_with_string_digits(lines):
    sum = 0
    for line in lines:
        digits = []
        for index in range(0, len(line)):
            if line[index].isdigit():
                digits.append(line[index])
            else:
                if index+4<len(line):
                    if (line[index:index+5]) == 'three':
                        digits.append(3)
                    if (line[index:index+5]) == 'seven':
                        digits.append(7)
                    if (line[index:index+5]) == 'eight':
                        digits.append(8)
                if index+3<len(line):
                    if (line[index:index+4]) == 'four':
                        digits.append(4)
                    if (line[index:index+4]) == 'five':
                        digits.append(5)
                    if (line[index:index+4]) == 'nine':
                        digits.append(9)
                if index+2<len(line):
                    if (line[index:index+3]) == 'one':
                        digits.append(1)
                    if (line[index:index+3]) == 'two':
                        digits.append(2)
                    if (line[index:index+3]) == 'six':
                        digits.append(6)                

        if len(digits) > 0:
            sum +=  int(digits[0])*10 + int(digits[len(digits)-1])
    return sum


if __name__ == '__main__':

    filename = sys.argv[1]
    file = open(filename, 'r')
    lines = []
    for line in file:
        lines.append(line)
    print(sum_calibration(lines))
    print(sum_calibration_with_string_digits(lines))


