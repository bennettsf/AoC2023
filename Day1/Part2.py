total = 0
numbers_spelled = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

try:
    with open('Day1/input.txt', 'r') as f:
        #make a list of the data split by newlines
        lines = [i for i in f.read().split('\n')]

        #iterate each string
        for line in lines:
            #list that contains all digits found in the current line (as strings)
            digits = []
            #go through each character in the line (enumerate used for checking spelled out nums with 'startswith')
            for i, char in enumerate(line):
                #check if char is already a digit, append it to the list
                if char.isdigit():
                    digits.append(char)
                #otherwise, check if the string from i to the end starts with any spelled numbers
                else:
                    for d, val in enumerate(numbers_spelled):
                        if line[i:].startswith(val):
                            digits.append(str(d + 1))
            #pull the first digit         
            first_digit = digits[0]
            #pull the last digit
            last_digit = digits[len(digits) - 1]  
            #string of first and last concatenated          
            current = first_digit + last_digit
            #convert to integer and add to the overall total
            total += int(current)
except:
    print('error reading thew file.')

print(total)