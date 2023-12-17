# https://adventofcode.com/2023/day/2#part2

import re
import traceback

try:
    with open('Day2/input.txt', 'r') as f:
        #read each line of the input
        lines = [i for i in f.read().split('\n')]
        # sum of 'squares' of 'fewest' number of colors per game
        sumOfSquares = 0
        
        # create a regex to parse the data using these delimeters
        delimeters = ':;'
        rePattern = '|'.join(map(re.escape, delimeters))
        # initiate a results dictionary
        results_dict = {}
        for line in lines:
            # reset green blue and red to 0 for each game (used as the highest pull of a color in the current game)
            green = 0
            blue = 0
            red = 0
            # parse the line using our regex pattern
            pullList = re.split(rePattern, line)
            # retrieve the game number
            game = int(pullList[0].replace("Game ", ""))
            pullList.pop(0)
            # create a list as our dictionary entry for the current game
            results_dict[game] = []
            
            for pull in pullList:
                # for each pull in our list of pulls, retrieve the number before each color
                green_num = re.search(r'(\d+)\s+green', pull)
                red_num = re.search(r'(\d+)\s+red', pull)
                blue_num = re.search(r'(\d+)\s+blue', pull)
                # initiate a base dictionary for the results
                curr_game_results = {'green': 0, 'red': 0, 'blue': 0}
                # check if the color exists in the pull, if so update the base dictionary with that number
                if green_num:
                    curr_game_results['green'] = int(green_num.group(1))
                if red_num:
                    curr_game_results['red'] = int(red_num.group(1))
                if blue_num:
                    curr_game_results['blue'] = int(blue_num.group(1))
                # append the pull results to the game's list within the dictionary
                results_dict[game].append(curr_game_results)

            # check each pull and update the largest number of each color for the current game
            for pull in results_dict[game]:
                if pull['green'] > green:
                    green = pull['green']
                if pull['red'] > red:
                    red = pull['red']
                if pull['blue'] > blue:
                    blue = pull['blue']
            # multiply those numbers together and add it to the sum
            sumOfSquares += (green * red * blue)
            
        print(sumOfSquares)    
except Exception as e:
    traceback.print_exc()
