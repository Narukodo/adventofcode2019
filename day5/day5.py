from pathlib import Path

#copy of day 2, but kept separate for record
inputs = list(map(int, (Path(__file__).parent / 'day5.input').read_text().split(',')))

def mode_val(mode, val, param_num, num_params):
    if param_num - 1 >= num_params:
        return -1
    if mode == 1:
        return val
    return inputs[val]

def store_at_pos(pos, val):
    inputs[pos] = val
    return 1

def jump_pc(pc_info, new_pc_val):
    pc_info['location'] = new_pc_val
    pc_info['has_jumped'] = True
    return 1

def get_args(pc, args_length, param_modes):
    args = []
    for offset in range(1, args_length + 1):
        args.append(inputs[pc + offset] if param_modes[offset - 1] == 0 else inputs[inputs[pc + offset]])
    return args

def run_op(op_code, ops_definitions, pc_info, pos1=0, pos2=0, res_pos=0, mode1=0, mode2=0, mode3=0):
    # mode_val = lambda mode, val: inputs[val] if mode == 0 else val
    has_param = lambda op, param_num: param_num in ops_definitions['num_params'][op]
    param1 = mode_val(mode1, pos1, 1, ops_definitions[op_code]['num_params'])
    param2 = mode_val(mode2, pos2, 2, ops_definitions[op_code]['num_params'])
    # print(param1, param2)
    # print(get_args(pc_info['location'], ops_definitions[op_code]['num_params'], [mode1, mode2, mode3]))
    ops_definitions[op_code]['run']([param1, param2], res_pos)
    

# part 1
def run_intcode_machine():
    pc_info = {
        'location': 0,
        'has_jumped': False
    }

    ops_definitions = {
        1: {
            'run': lambda args, res_pos: store_at_pos(res_pos, args[0] + args[1]),
            'op_res_pos': lambda pc: inputs[pc + 3],
            'op_args': lambda pc: (inputs[pc + 1], inputs[pc + 2]),
            'num_params': 3,
            'pc_inc_val': lambda has_jumped: 4
        },
        2: {
            'run': lambda args, res_pos: store_at_pos(res_pos, args[0] * args[1]),
            'op_res_pos': lambda pc: inputs[pc + 3],
            'op_args': lambda pc: (inputs[pc + 1], inputs[pc + 2]),
            'num_params': 3,
            'pc_inc_val': lambda has_jumped: 4
        },
        3: {
            'run': lambda args, res_pos: store_at_pos(res_pos, int(input())),
            'op_res_pos': lambda pc: inputs[pc + 1],
            'op_args': lambda pc: (-1, -1),
            'num_params': 1,
            'pc_inc_val': lambda has_jumped: 2
        },
        4: {
            'run': lambda args, res_pos: print(args[0]),
            'op_res_pos': lambda pc: -1,
            'op_args': lambda pc: (inputs[pc + 1], -1),
            'num_params': 1,
            'pc_inc_val': lambda has_jumped: 2
        },
        5: {
            'run': lambda args, res_pos: jump_pc(pc_info, args[1]) if bool(args[0]) else None,
            'op_res_pos': lambda pc: -1,
            'op_args': lambda pc: (inputs[pc + 1], inputs[pc + 2]),
            'num_params': 2,
            'pc_inc_val': lambda has_jumped: 3 if not has_jumped else 0
        },
        6: {
            'run': lambda args, res_pos: jump_pc(pc_info, args[1]) if not bool(args[0]) else None,
            'op_res_pos': lambda pc: -1,
            'op_args': lambda pc: (inputs[pc + 1], inputs[pc + 2]),
            'num_params': 2,
            'pc_inc_val': lambda has_jumped: 3 if not has_jumped else 0
        },
        7: {
            'run': lambda args, res_pos: store_at_pos(res_pos, int(args[0] < args[1])),
            'op_res_pos': lambda pc: inputs[pc + 3],
            'op_args': lambda pc: (inputs[pc + 1], inputs[pc + 2]),
            'num_params': 3,
            'pc_inc_val': lambda has_jumped: 4
        },
        8: {
            'run': lambda args, res_pos: store_at_pos(res_pos, int(args[0] == args[1])),
            'op_res_pos': lambda pc: inputs[pc + 3],
            'op_args': lambda pc: (inputs[pc + 1], inputs[pc + 2]),
            'num_params': 3,
            'pc_inc_val': lambda has_jumped: 4
        }
    }
    while pc_info['location'] < len(inputs) and inputs[pc_info['location']] != 99:

        # get op code and param modes
        param_mode = lambda param_code: (int(param_code[3:]), int(param_code[2]), int(param_code[1]), int(param_code[0])) 
        op_code, mode1, mode2, mode3 = param_mode(str(inputs[pc_info['location']]).zfill(5))

        # get param and result positions
        pos1, pos2 = ops_definitions[op_code]['op_args'](pc_info['location'])
        pos3 = ops_definitions[op_code]['op_res_pos'](pc_info['location'])

        # run op
        run_op(op_code, ops_definitions, pc_info, pos1, pos2, pos3, mode1, mode2, mode3)

        # increment pc
        pc_info['location'] += ops_definitions[op_code]['pc_inc_val'](pc_info['has_jumped'])
        pc_info['has_jumped'] = False

run_intcode_machine()
