import os
import re

#Bulding the pattern of data
def data_split(two_lines):
    pat = re.compile('DATE= (\d+\/\d+\/\d+) TIME= (\d+\:\d+\:\d+)_N_(.{9}_.{4})_(.{4})_(.{3})\s+CYCLE_TIME: (\d+) MIN, (\d+\.\d+) SEC')
    answer = re.search(pat, two_lines)
    if answer is not None: #getting rid of None lines
        return answer.groups()

#definig the class that will hold the information from the file
class MachineAction:
    def __init__(self, date, time, item, prog, mpf, minutes, seconds):
        self.date = date
        self.time = time
        self.item = item
        self.prog = prog
        self.mpf = mpf
        self.minutes = minutes
        self.seconds = seconds

#loading files
my_machine_actions = []

dir_name = r'C:\Users\IMOE001\OneDrive - Matan Investing in community\Documents\Naya\project 1'
f_name = (f'{dir_name}\MAT.MPF')
with open(f_name, encoding = 'utf-8') as f:

    # constructing the data to one string
    for i, line in enumerate(f):
        if i % 3 == 0:  #look at the first line and
            line1 = line[:-1]

        elif i % 3 == 1:
            line2 = line[:-1]
            unified_line = line1 + line2
            answer = data_split(unified_line)
            if answer is not None:
                line_date, line_time, line_item, line_prog, line_mpf, line_min, line_sec  = answer
                my_ma = MachineAction(line_date, line_time, line_item, line_prog, line_mpf, line_min, line_sec)
                my_machine_actions.append(my_ma)
            else:
                print(unified_line)
        elif i % 3 == 2:
            continue


