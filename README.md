# Advent of Code 2019
My own solutions for Advent of Code 2019 (Started May 14, 2020)
Solutions uploaded every day except for Sundays.
Inputs ignored

Solution explanations will be typed here if the answer isn't immediately obvious.

Day 2 (part 2)
- Trying out every combination would take too long. Since this is a puzzle, there's probably a pattern here.
- Observed that incrementing pos 1 results in a 900000-unit increase in the end result (for my inputs)
- Observed that incrementing pos 2 results in a 1-unit increase in the end result (for my inputs)
- Therefore, we follow the function of `TARGET_VALUE = INITIAL_VALUE + 900000 * noun + 1 * verb`
- `noun` and `verb` are bound by the length of input since they specify positions within the input
- To make this configurable for others who'd like to try running it, constants are used (`NOUN_MULTIPLIER` and `VERB_MULTIPLIER` respectively)

Day 3
Did a sweep from left to right to see if there are any intersections. My first instinct was to brute force, but I wanted to try this out again. The code's a little buggy, but it seems to work for my input, so I'm just leaving it be.

Day 5
The Intcode computer's given a full refactor to run on rules rather than if statements. The hope is to make the infrastructure scalable. Adding an operation is just a matter of adding its definition, how much to increment PC by if the operation is encountered, and specifying the number of args and where to store its result, if it has one. Due to Python 3.7's restrictions on lambdas, auxiliary functions have to be made to allow things such as assignment. Assignment feature for lambdas have been added in Python3.8 but since most people are likely still on 3.7, I will be keeping this for now.
