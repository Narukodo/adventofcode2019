from pathlib import Path

#copy of day 2, but kept separate for record
inputs = list(map(int, (Path(__file__).parent / 'day5.input').read_text().split(',')))

def mode_val(mode, val, param_num, params):
    if param_num not in params:
        return -1
    if mode == 1:
        return val
    return inputs[val]

def assign(pos, val):
    inputs[pos] = val
    return 1

def change_pc(pc_info, new_pc_val):
    pc_info['location'] = new_pc_val
    pc_info['has_jumped'] = True
    return 1

def ops(op_code, machine, pc_info, pos1=0, pos2=0, res_pos=0, mode1=0, mode2=0, mode3=0):
    # mode_val = lambda mode, val: inputs[val] if mode == 0 else val
    has_param = lambda op, param_num: param_num in machine['params'][op]
    param1 = mode_val(mode1, pos1, 1, machine['params'][op_code])
    param2 = mode_val(mode2, pos2, 2, machine['params'][op_code])
    machine['ops'][op_code](param1, param2, res_pos)
    

# part 1
def run_ops():
    pc_info = {
        'location': 0,
        'pc_inc_val': [
            lambda has_jumped: 4,
            lambda has_jumped: 4,
            lambda has_jumped: 2,
            lambda has_jumped: 2,
            lambda has_jumped: 3 if has_jumped else 0,
            lambda has_jumped: 3 if has_jumped else 0,
            lambda has_jumped: 4,
            lambda has_jumped: 4
        ],
        'has_jumped': False
    }

    machine = {
        'ops': [
            lambda a, b, res_pos: assign(res_pos, a + b),
            lambda a, b, res_pos: assign(res_pos, a * b),
            lambda a, b, res_pos: assign(res_pos, int(input())),
            lambda a, b, res_pos: print(a),
            lambda a, b, res_pos: change_pc(pc_info, b) if bool(a) else None,
            lambda a, b, res_pos: change_pc(pc_info, b) if not bool(a) else None,
            lambda a, b, res_pos: assign(res_pos, int(a < b)),
            lambda a, b, res_pos: assign(res_pos, int(a == b))
        ],
        'op_res_pos': [
            lambda pc: inputs[pc + 3],
            lambda pc: inputs[pc + 3],
            lambda pc: inputs[pc + 1],
            lambda pc: -1,
            lambda pc: -1,
            lambda pc: -1,
            lambda pc: inputs[pc + 3],
            lambda pc: inputs[pc + 3]
        ],
        'op_param_pos': [
            lambda pc: (inputs[pc + 1], inputs[pc + 2]),
            lambda pc: (inputs[pc + 1], inputs[pc + 2]),
            lambda pc: (-1, -1),
            lambda pc: (inputs[pc + 1], -1),
            lambda pc: (inputs[pc + 1], inputs[pc + 2]),
            lambda pc: (inputs[pc + 1], inputs[pc + 2]),
            lambda pc: (inputs[pc + 1], inputs[pc + 2]),
            lambda pc: (inputs[pc + 1], inputs[pc + 2])
        ],
        'params': [
            [1, 2, 3],
            [1, 2, 3],
            [1],
            [1],
            [1, 2],
            [1, 2],
            [1, 2, 3],
            [1, 2, 3]
        ]
    }
    # pc_add = 4
    # pc = 0
    while pc_info['location'] < len(inputs) and inputs[pc_info['location']] != 99:

        # op p1, p2, p3, op_code must be of kind ABCDE
        param_mode = lambda param_code: (int(param_code[4:]) - 1, int(param_code[2]), int(param_code[1]), int(param_code[0])) 
        op_code, mode1, mode2, mode3 = param_mode(str(inputs[pc_info['location']]).zfill(5))
        if op_code + 1 == 5:
            print(inputs[pc_info['location']], inputs[pc_info['location'] + 1], inputs[pc_info['location'] + 2])
        pos1, pos2 = machine['op_param_pos'][op_code](pc_info['location'])
        pos3 = machine['op_res_pos'][op_code](pc_info['location'])
        ops(op_code, machine, pc_info, pos1, pos2, pos3, mode1, mode2, mode3)
        pc_info['location'] += pc_info['pc_inc_val'][op_code](pc_info['has_jumped'])
        pc_info['has_jumped'] = 0

run_ops()
