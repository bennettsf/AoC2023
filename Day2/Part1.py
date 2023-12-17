# https://adventofcode.com/2023/day/2

import re
import traceback

try:
    with open('Day2/input.txt', 'r') as f:
        # read each line of the input
        lines = [i for i in f.read().split('\n')]
        # sum of game numbers that pass the test
        possibleGamesTotal = 0
        # create a regex to parse the data using these delimiters
        delimiters = ':;'
        rePattern = '|'.join(map(re.escape, delimiters))
        # initiate a results dictionary
        results_dict = {}
        for line in lines:
            # parse the line using our regex pattern
            pullList = re.split(rePattern, line)
            # retrieve the game number
            game = int(pullList[0].replace("Game ", ""))
            pullList.pop(0)
            # create a list as our dictionary entry for the current game
            results_dict[game] = []
            # start with a False pass
            passed = False
            
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

            # iterate the new entries in the results dict
            for pull in results_dict[game]:
                # if the pull passes, set passed to True
                if pull['green'] <= 13 and pull['red'] <= 12 and pull['blue'] <= 14:
                    passed = True
                # otherwise set to False and break
                else:
                    passed = False
                    break
            # after checking each pull for the current game, check if we ended with True
            if passed:
                # if so, add the game number to the total sum
                possibleGamesTotal += game

        print(possibleGamesTotal)


except Exception as e:
    traceback.print_exc()
