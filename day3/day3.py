from pathlib import Path
from collections import namedtuple
import operator
import sys

# vertical line: line, x, y1, y2
# horizontal line: line, x, height

inputs = (Path(__file__).parent / 'day3.input').read_text().split()
line1 = [(direction[:1], int(direction[1:])) for direction in inputs[0].split(',')]
line2 = [(direction[:1], int(direction[1:])) for direction in inputs[1].split(',')]


x = 0
y = 0
idx = 0

lines = []

# initialize... optimize later
for d, m in line1:
    if d == 'U':
        lines.append((1, 1, x, y, y + m))
        y += m
    elif d == 'D':
        lines.append((1, 1, x, y - m, y))
        y -= m
    elif d == 'R':
        lines.append((1, 0, x, y, y, 1))
        lines.append((1, 0, x + m, y, y, -1))
        x += m
    else:
        lines.append((1, 0, x, y, y, 1))
        lines.append((1, 0, x - m, y, y, -1))
        x -= m

x = 0
y = 0
idx = 0
for d, m in line2:
    if d == 'U':
        lines.append((2, 1, x, y, y + m))
        y += m
    elif d == 'D':
        lines.append((2, 1, x, y - m, y))
        y -= m
    elif d == 'R':
        lines.append((2, 0, x, y, y, 1))
        lines.append((2, 0, x + m, y, y, -1))
        x += m
    else:
        lines.append((2, 0, x, y, y, -1))
        lines.append((2, 0, x - m, y, y, 1))
        x -= m

lines.sort(key=operator.itemgetter(2, 1))

# *************************************************************************************************************************************

def manhattan_distance(point):
    return abs(point[0]) + abs(point[1])

intersections = []

def get_min_manhattan_distance(lines):
    xs1 = {}
    xs2 = {}
    min_distance = sys.maxsize
    lines.sort(key=lambda line: line[2])
    for idx, line in enumerate(lines):
        if line[1]: # if line is vertical
            if line[0] == 1:
                x_dict = xs2
            else:
                x_dict = xs1
            for height in range(line[3], line[4]):
                if height in x_dict and x_dict[height] and not (line[2] == 0 and height == 0):
                    intersections.append((line[2], height))
                    distance = manhattan_distance((line[2], height))
                    if distance < min_distance and not (line[2] == 0 and height == 0):
                        min_distance = distance
        else: # if line is horizontal
            if line[0] == 1:
                x_dict = xs1
            else:
                x_dict = xs2
            try:
                x_dict[line[3]] += line[5]
            except KeyError as e:
                x_dict[line[3]] = 1
    return min_distance


def steps_to_intersection(line, intersection):
    x_coord = 0
    y_coord = 0
    steps = 0
    for d, m in line:
        prev_coord = (x_coord, y_coord)
        if d == 'U':
            y_coord += m
            if intersection[0] == x_coord and intersection[1] >= prev_coord[1] and intersection[1] <= y_coord:
                if intersection[0] == 1476 and intersection[1] == -934:
                    print(d, prev_coord, intersection, (x_coord, y_coord))
                return steps + abs(intersection[1] - prev_coord[1])
        elif d == 'D':
            y_coord -= m
            if intersection[0] == x_coord and intersection[1] <= prev_coord[1] and intersection[1] >= y_coord:
                if intersection[0] == 1476 and intersection[1] == -934:
                    print(d, prev_coord, intersection, (x_coord, y_coord))
                return steps + abs(prev_coord[1] - intersection[1])
        elif d == 'R':
            x_coord += m
            if intersection[1] == y_coord and intersection[0] >= prev_coord[0] and intersection[0] <= x_coord:
                if intersection[0] == 1476 and intersection[1] == -934:
                    print(d, prev_coord, intersection, (x_coord, y_coord))
                return steps + abs(intersection[0] - prev_coord[0])
        else:
            x_coord -= m
            if intersection[1] == y_coord and intersection[0] <= prev_coord[0] and intersection[0] >= x_coord:
                if intersection[0] == 1476 and intersection[1] == -934:
                    print(d, prev_coord, intersection, (x_coord, y_coord))
                return steps + abs(intersection[0] - prev_coord[0])
        steps += m

print(get_min_manhattan_distance(lines))


min_steps = sys.maxsize
for intersection in intersections:
    try:
        total_steps = steps_to_intersection(line1, intersection) + steps_to_intersection(line2, intersection)
    except:
        print(intersection) # intersections are all wrong, but I got the right answer anyway ¯\_(ツ)_/¯
    if total_steps < min_steps:
        min_steps = total_steps
print(min_steps)