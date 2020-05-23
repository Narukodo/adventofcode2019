from pathlib import Path

#copy of day 2, but kept separate for record
inputs = list(map(int, (Path(__file__).parent / 'day5.input').read_text().split(',')))

# ================= SYSTEM INIT =====================
pc_info = {
    'location': 0,
    'has_jumped': False
}


# ================= AUXILIARY FUNCTIONS =============
def store_at_pos(pos, val):
    inputs[pos] = val
    return 1


def pc_jump_by(new_pc_val):
    pc_info['location'] = new_pc_val
    pc_info['has_jumped'] = True
    return 1


# ================= HELPER FUNCTIONS ================
def get_current_operation_args(pc, args_length, param_modes):
    args = []
    for offset in range(1, args_length + 1):
        args.append(inputs[pc + offset] if param_modes[offset - 1] == 1 else inputs[inputs[pc + offset]])
    return args


# ================= DEFINITIONS =====================
OPCODES = {
    1: {
        'run_operation': lambda args, res_pos: store_at_pos(res_pos, args[0] + args[1]),
        'get_result_position': lambda pc: inputs[pc + 3],
        'number_of_args': 2,
        'pc_increment_by': lambda has_jumped: 4
    },
    2: {
        'run_operation': lambda args, res_pos: store_at_pos(res_pos, args[0] * args[1]),
        'get_result_position': lambda pc: inputs[pc + 3],
        'number_of_args': 2,
        'pc_increment_by': lambda has_jumped: 4
    },
    3: {
        'run_operation': lambda args, res_pos: store_at_pos(res_pos, int(input())),
        'get_result_position': lambda pc: inputs[pc + 1],
        'number_of_args': 0,
        'pc_increment_by': lambda has_jumped: 2
    },
    4: {
        'run_operation': lambda args, res_pos: print(args[0]),
        'get_result_position': lambda pc: -1,
        'number_of_args': 1,
        'pc_increment_by': lambda has_jumped: 2
    },
    5: {
        'run_operation': lambda args, res_pos: pc_jump_by(args[1]) if bool(args[0]) else None,
        'get_result_position': lambda pc: -1,
        'number_of_args': 2,
        'pc_increment_by': lambda has_jumped: 3 if not has_jumped else 0
    },
    6: {
        'run_operation': lambda args, res_pos: pc_jump_by(args[1]) if not bool(args[0]) else None,
        'get_result_position': lambda pc: -1,
        'number_of_args': 2,
        'pc_increment_by': lambda has_jumped: 3 if not has_jumped else 0
    },
    7: {
        'run_operation': lambda args, res_pos: store_at_pos(res_pos, int(args[0] < args[1])),
        'get_result_position': lambda pc: inputs[pc + 3],
        'number_of_args': 2,
        'pc_increment_by': lambda has_jumped: 4
    },
    8: {
        'run_operation': lambda args, res_pos: store_at_pos(res_pos, int(args[0] == args[1])),
        'get_result_position': lambda pc: inputs[pc + 3],
        'number_of_args': 2,
        'pc_increment_by': lambda has_jumped: 4
    }
}
    
# part 1
def run_intcode_machine():
    while pc_info['location'] < len(inputs) and inputs[pc_info['location']] != 99:

        # get op code and param modes
        param_mode = lambda param_code: (int(param_code[3:]), [int(mode) for mode in list(param_code[:3])][::-1]) 
        op_code, modes = param_mode(str(inputs[pc_info['location']]).zfill(5))

        # get args and result positions
        args = get_current_operation_args(pc_info['location'], OPCODES[op_code]['number_of_args'], modes)
        res_pos = OPCODES[op_code]['get_result_position'](pc_info['location'])

        # run op
        OPCODES[op_code]['run_operation'](args, res_pos)

        # increment pc
        pc_info['location'] += OPCODES[op_code]['pc_increment_by'](pc_info['has_jumped'])
        pc_info['has_jumped'] = False

run_intcode_machine()
