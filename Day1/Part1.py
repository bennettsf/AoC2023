total = 0

try:
    with open('Day1/input.txt', 'r') as f:
        lines = [i for i in f.read().split('\n')]
        
        for line in lines:
            digits = []
            for char in line:
                if char.isdigit():
                    digits.append(str(char))
            current = digits[0] + digits[len(digits) - 1]
            total += int(current)
except:
    print('error reading the file.')

print(total)