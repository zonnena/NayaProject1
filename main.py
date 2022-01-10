import os
import re

#Bulding the pattern of data - making each two lines one string
# def data_split(two_lines):
#     # pat = re.compile('DATE= (\d+\/\d+\/\d+) TIME= (\d+\:\d+\:\d+)_N_(.{9}_.{4})_(.{3,5})_(.{3})\s+CYCLE_TIME: (\d+) MIN, (\d+\.\d+) SEC')
#     # answer = re.search(pat, two_lines)
#
#     if answer is not None: #getting rid of None lines
#         return answer.groups()
#     else:
#         pat = re.compile('DATE= (\d+\/\d+\/\d+) TIME= (\d+\:\d+\:\d+)_N_(.{9}_.{4})_(.{3,5})__(.{2,2}_(.{3})\s+CYCLE_TIME: (\d+) MIN, (\d+\.\d+) SEC')
#         answer = re.search(pat, two_lines)

#Making a list of all unique non 2CSH
my_set = set()
my_set_2CSJ = set()

def data_split(line1,line2):
    line1_split = line1.split(" ")
    cycle_text = "CYCLE_TIME:"
    cycle_time_start = line2.find("CYCLE_TIME:")
    cycle_time_end = cycle_time_start + len(cycle_text)
    date = line1_split[1]
    time = line1_split[3]
    cycle = line2[cycle_time_end:]

    items_etc = str(line2[:cycle_time_start].strip()).split("_")
    proper_item = None
    if items_etc[2].startswith(('2CSH', '16T7302-805', '2CSJ10500', '16T7302')):
        proper_item = items_etc[2]
    #if not items_etc[3].startswith('0'):
    # my_set.add(items_etc[(3)])
    strange_prog = None
    if items_etc[3].startswith(('805', 'CAL', 'JOGLE', 'CHECK', '3-HINGE', 'HEAD', '397', 'T99')):
        strange_prog = items_etc[3]

    return date, time, cycle, proper_item, strange_prog

#definig the class that will hold the information from the file
class MachineAction:
    def __init__(self, date, time, item, prog, mpf, minutes, seconds, to = None):
        self.date = date
        self.time = time
        self.item = item
        self.prog = prog
        self.mpf = mpf
        self.minutes = minutes
        self.seconds = seconds
        self.to = to








#loading files
my_machine_actions = [] #making an empty list for the data

dir_name = r'C:\Users\IMOE001\OneDrive - Matan Investing in community\Documents\Naya\project 1' # file location
f_name = (f'{dir_name}\MAT.MPF') #loading the file
with open(f_name, encoding = 'utf-8') as f: #encoding the file

    # constructing the data to one string
    for i, line in enumerate(f):
        if i % 3 == 0:  #look at the first line and
            line1 = line[:-1]
        elif i % 3 == 1:
            line2 = line[:-1]
            unified_line = line1 + line2
            answer = data_split(line1, line2)
            #print(i, answer)
            line_date, line_time, line_proper, line_strange, line_cycle  = answer
            #     my_ma = MachineAction(date = line_date, time = line_time, item = line_item, prog = line_prog, mpf = line_mpf, minutes = line_min, seconds = line_sec)
            #     my_machine_actions.append(my_ma)
            # else:
            #     print(unified_line)


        elif i % 3 == 2:
            continue



