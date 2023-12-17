# https://adventofcode.com/2023/day/3

import re
import traceback

try:
    with open('Day3/input.txt', 'r') as f:
        # read each line of the input
        lines = [i for i in f.read().split('\n')]

        # empty line used for prev line of first line and next line of last line
        empty_line = '..................................................................................................................................'
        # regex pattern to find symbols other than periods/alphanumeric characters
        symbol_pattern = re.compile(r'[^a-zA-Z0-9.]')
        #part total count starting at 0
        part_total = 0

        for line_num, line in enumerate(lines):
            
            # find each number of the current line
            line_nums = re.finditer(r'(\d+)', line)
            # create a dictionary using the number as a key and list of the start/end index as the value
            num_dict = {int(match.group()): [match.start(), match.end() - 1] for match in line_nums}

            # iterate each number in the current line
            for num in num_dict:
                # if we're at the first line, set prev_line to empty_line, otherwise check the actual previous line
                if line_num == 0:
                    prev_line = empty_line
                else:
                    prev_line = lines[line_num - 1]

                # if we're at the last line, set next_line to empty_line, otherwise check the actual next line
                if line == lines[-1]:
                    next_line = empty_line
                else:
                    next_line = lines[line_num + 1]

                # index seach start/end to find symbols
                start_search = num_dict[num][0] - 1
                end_search = num_dict[num][1] + 2

                # check prev, curr, and next lines for symbols within the start/end search threshold of a number
                prev_line_search = bool(symbol_pattern.search(prev_line[start_search:end_search]))
                next_line_search = bool(symbol_pattern.search(next_line[start_search:end_search]))
                current_line_search = bool(symbol_pattern.search(line[start_search:end_search]))

                # return True if a symbol is found and add that number to the current part total
                if prev_line_search or next_line_search or current_line_search:
                    print(str(part_total) + ' ' + str(num))
                    part_total += num
                    

        print(part_total)
            
except Exception as e:
    traceback.print_exc()
