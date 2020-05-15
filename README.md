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
