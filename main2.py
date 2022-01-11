import os
import re
from _datetime import datetime, timedelta


#defining the functions

#splitting the lines
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




#making a total work time for every day
def date_list():
    my_date_list = []
    my_time_dict = {}
    for d in range(1, (len(my_machine_actions)-1)):
        if my_machine_actions[d].l_date == my_machine_actions[d+1].l_date:
            my_date_list.append(my_machine_actions[d].l_time_diff)

        else:
            #print(len(my_date_list) ,my_machine_actions[d].l_date)
            #sum(my_date_list)
            #print(my_time_dict)
            #print(sum(my_date_list, timedelta()))
            my_time_dict[str(my_machine_actions[d].l_date)] = str(sum(my_date_list, timedelta()))
            my_date_list = []
    print(my_time_dict)

# def total_time():
#     my_total_time = 0
#     for el in range(0, len(date_list())):
#         total = total + data_list[el]
#         print(f'The sum of work on day is {total_time()}')

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
date_list()
#total_time()

#calculating the sum of work on a given day
day_dates = []
def day_total():
    for day in range(1, (len(my_machine_actions)-1)):
        day_dates.append(my_machine_actions[i].l_date)
        # day_total = (my_machine_actions[i].l_time_diff) + (my_machine_actions[i+1].l_time_diff)
        # print(day_total)
