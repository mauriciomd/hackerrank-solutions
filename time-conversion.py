#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time_formatted = ''
    
    if 'AM' in s:
        time = s.replace('AM', '').split(':')
        if time[0] == '12':
            time_formatted = f'00:{time[1]}:{time[2]}'
        else:
            time_formatted = f'{time[0]}:{time[1]}:{time[2]}'
    else:
        time = s.replace('PM', '').split(':')
        if time[0] == '12':
            time_formatted = f'{time[0]}:{time[1]}:{time[2]}'
        else:
            time_formatted = f'{int(time[0]) + 12}:{time[1]}:{time[2]}'
    
    return time_formatted

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
