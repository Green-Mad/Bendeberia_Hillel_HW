# You are given a string representing a sequence of N arrows, each pointing in one of the four
# cardinal directions: up (^), down (v), left(<) or right (>).
# Write a function that, given a string S denoting the directions of the arrows, returns
# the minimum number of arrows that must be rotated to make them all point in the same
# direction
# Examples:
# 1. Given S = "^vv<v", the function should return 2. After rotating both the first ('^') and fourth ('<')
# arrows downwards ('v'), all of the arrows would point down.
# 2. Given S = "v>>>vv", the function should return 3. After rotating the first, fifth, and sixth arrow
# rightwards, all of the arrows would point right.
# 3. Given S = "<<<" the function should return 0. All of the arrows already point left.
# Assume that:
# string S is made only of the following characters: '^', 'v, '< and/or'>'.

def min_arrow_rotations(S: str) -> int:
    rotations = {
        '^': {'^': 0, 'v': 1, '<': 1, '>': 1},
        'v': {'^': 1, 'v': 0, '<': 1, '>': 1},
        '<': {'^': 1, 'v': 1, '<': 0, '>': 1},
        '>': {'^': 1, 'v': 1, '<': 1, '>': 0}
    }
    directions = {'^', 'v', '<', '>'}
    min_rotations = float('inf')

    for direction in directions:
        rotations_needed = 0
        for arrow in S:
            rotations_needed += rotations[arrow][direction]
        min_rotations = min(min_rotations, rotations_needed)

    return min_rotations

S = "^vv<v"
result = min_arrow_rotations(S)
print(result)

S = "v>>>vv"
result = min_arrow_rotations(S)
print(result)

S = "<<<"
result = min_arrow_rotations(S)
print(result)
