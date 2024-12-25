#!/usr/bin/python3
import sys

def sum_games(lines):
    sum = 0
    for line in lines:
        line_split = line.split(': ')
        game_number = int(line_split[0].split(' ')[1])
        random_gets=line_split[1].split('; ')
        maxs = {}
        for rg in random_gets:
            colors = rg.split(', ')
            locals = {}
            for color in colors:
                color_name = color.split(' ')[1]
                color_count = int(color.split(' ')[0])
                if color_name in locals:
                    locals[color_name] = color_count + locals[color_name]
                else:
                    locals[color_name] = color_count
            for color in locals.keys():
                if color in maxs:
                    maxs[color] = max(maxs[color], locals[color])
                else:
                    maxs[color] = locals[color]
        #only 12 red cubes, 13 green cubes, and 14 blue cubes
        if maxs.get('red', 0) <= 12 and maxs.get('green', 0) <= 13 and maxs.get('blue', 0) <= 14:
            sum += game_number
    return sum

def power_games(lines):
    sum = 0
    for line in lines:
        line_split = line.split(': ')
        game_number = int(line_split[0].split(' ')[1])
        random_gets=line_split[1].split('; ')
        maxs = {}
        for rg in random_gets:
            colors = rg.split(', ')
            locals = {}
            for color in colors:
                color_name = color.split(' ')[1]
                color_count = int(color.split(' ')[0])
                if color_name in locals:
                    locals[color_name] = color_count + locals[color_name]
                else:
                    locals[color_name] = color_count
            for color in locals.keys():
                if color in maxs:
                    maxs[color] = max(maxs[color], locals[color])
                else:
                    maxs[color] = locals[color]
        sum += maxs.get('red',1) * maxs.get('green',1) * maxs.get('blue', 1)
    return sum


if __name__ == '__main__':

    filename = sys.argv[1]
    
    file = open(filename, 'r')
    lines = []
    for line in file:
        lines.append(line.strip())
    print(sum_games(lines))
    print(power_games(lines))


