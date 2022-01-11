import os
import re
from _datetime import datetime




#Making a list of all unique non 2CSH
my_set = set()
my_set_2CSJ = set()

def data_split(line1,line2):
    line1_split = line1.split(" ")
    cycle_text = "CYCLE_TIME:"
    cycle_time_start = line2.find("CYCLE_TIME:")
    cycle_time_end = cycle_time_start + len(cycle_text)
    l_date = line1_split[1]
    l_time = line1_split[3]
    cycle = str(line2[cycle_time_end:].strip()).split(',')
    items_etc = str(line2[:cycle_time_start].strip()).split("_")
    l_item = items_etc[2]+'_'+items_etc[3]
    l_prog = items_etc[4]
    l_min = cycle[0].split(' ')[0]
    l_sec = cycle[1].split(' ')[1]

    return l_date, l_time, l_item, l_prog, l_min, l_sec

# calculating the time difference between two actions
def machine_action_time_diff():
    for i in range(1, (len(my_machine_actions)-1)):
        my_machine_actions[i].l_time_diff = my_machine_actions[i+1].l_datetime - my_machine_actions[i].l_datetime
        #print(my_machine_actions[i].l_time_diff)


#definig the class that will hold the information from the file
class MachineAction:
    def __init__(self, l_date, l_time, l_item, l_prog, l_min, l_sec):
        self.l_datetime = datetime.strptime( l_date + ' ' + l_time, '%d/%m/%y %H:%M:%S')
        self.l_date = datetime.strptime(l_date, '%d/%m/%y').date()
        self.l_time = datetime.strptime(l_time, '%H:%M:%S').time()
        self.l_item = l_item
        self.l_prog = l_prog
        self.l_min = l_min
        self.l_sec = l_sec
        self.l_time_diff = None


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
            l_date, l_time, l_item, l_prog, l_min, l_sec  = answer
            my_ma = MachineAction(l_date = l_date, l_time = l_time, l_item = l_item, l_prog = l_prog, l_min = l_min, l_sec = l_sec)
            my_machine_actions.append(my_ma)
            # for obj in my_machine_actions:
            #     print(obj.l_date, obj.l_item, obj.l_prog, obj.l_min, obj.l_sec, sep=' ')
            # else:
            #     print(unified_line)


        elif i % 3 == 2:
            continue
machine_action_time_diff()


#date_obj = datetime. strptime(l_date, '%d/%m/%y')
#print(date_obj)
# time_obj = datetime.strptime(l_time, '%H:%M:%S')
#
# print(time_obj)

for obj in my_machine_actions:
    #print(obj.l_date, obj.l_time, obj.l_item, obj.l_prog, obj.l_min, obj.l_sec, sep=' ')
    print(obj.l_time_diff,  sep=' ')
#print(len(my_machine_actions))


