from pathlib import Path

original_inputs = list(map(int, (Path(__file__).parent / 'day2.input').read_text().split(',')))
inputs = original_inputs.copy()

inputs[1] = 12 # + 900000
inputs[2] = 2 # + 1

# part 1
def run_ops():
    for op_idx in range(int(len(inputs)/4)):
        if inputs[op_idx * 4] == 99:
            return inputs[0]
        else:
            actual_idx = op_idx * 4
            op = inputs[actual_idx]
            pos1 = inputs[actual_idx + 1]
            pos2 = inputs[actual_idx + 2]
            res_pos = inputs[actual_idx + 3]
            if op == 1:
                inputs[res_pos] = inputs[pos1] + inputs[pos2]
            elif op == 2:
                inputs[res_pos] = inputs[pos1] * inputs[pos2]
            else:
                print('something went wrong')

print(run_ops())

# part 2
INITIAL_VALUE = 1690717
TARGET_NUM = 19690720 - INITIAL_VALUE 

NOUN_MULTIPLIER = 900000 # inputs[0] increments by 900000 for every noun increment
VERB_MULTIPLIER = 1 # verb increments increases inputs[0] by factor of 1

# b = 1690717
for noun in range(len(original_inputs)):
    verb = int((TARGET_NUM - noun * NOUN_MULTIPLIER)/VERB_MULTIPLIER)
    if verb < len(original_inputs) and verb > 0:
        print(noun, verb, 100 * noun + verb)
