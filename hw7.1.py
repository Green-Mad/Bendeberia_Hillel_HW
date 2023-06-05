# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

import sys

def my_print(*args, sep=' ', end='\n', file=sys.stdout, flush=False):
    output = sep.join(str(arg) for arg in args)

    output += end
    file.write(output)

    if flush:
        file.flush()

my_print('Hello', 'world!')

with open('First_task_print.txt', 'w') as file:
    my_print('Hello', 'world!', file=file)
