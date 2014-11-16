from pdb import set_trace
from collections import OrderedDict

# API
# -------------------------
def increase_value( max_value_file,
                    curr_value_file,
                    step = 10 ):
    cur_val = get_num_from_file(curr_value_file)
    max_val = get_num_from_file(max_value_file)
    next_higher = get_next_higher_value(cur_val, max_val, step)
    write_num_to_file(curr_value_file, next_higher)

def decrease_value( max_value_file,
                    curr_value_file,
                    step = 10):
    cur_val = get_num_from_file(curr_value_file)
    max_val = get_num_from_file(max_value_file)
    next_lower = get_next_lower_value(cur_val, max_val, step)
    write_num_to_file(curr_value_file, next_lower)

# -------------------------
def get_next_lower_value( cur_val, max_val, intervals = 10 ):
    intervals = get_intervals(max_val, intervals)
    less = [ x for x in intervals if x < cur_val ]
    return less[0]

def get_next_higher_value( cur_val, max_val, intervals = 10 ):
    intervals = get_intervals(max_val, intervals)
    more = [ x for x in intervals if x > cur_val ]
    # set_trace()
    return more[-1]

'''
Given a starting integer, number of intervals, and asc or desc, it will
return an array with increments/decrements in the number of intervals.

example: 12, 4, decrement => [9, 6, 3, 0]
'''
def get_intervals( starting_num, intervals = 4):
    gap = max(1,int(starting_num / intervals)) * -1

    final_num = int(starting_num + ( gap * intervals ) + gap)
    items = [ max(x,0) for x in range( starting_num + gap, final_num, gap )]
    no_dups = list(OrderedDict.fromkeys(items))
    no_dups.insert(0, starting_num)
    return no_dups

def get_num_from_file(filename):
    with open(filename) as f:
        content = f.readlines()
    # set_trace()
    return int(content[0])

def write_num_to_file(filename, number):
    with open(filename, 'w') as the_file:
        the_file.write(str(number) + "\n")
