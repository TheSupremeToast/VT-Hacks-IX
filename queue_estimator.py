import os
from os.path import exists
import pandas as pd
import datetime
from structures.TAUser import *

histfile = './input/history.csv'

# create dataframe with fields:
# TA name, start_time, end_time
#
# track time from assignment to unassignment


#
# Read history csv if it exists
# 
def read_history():
    if (not exists(histfile)):
        with open(histfile, 'w') as f:
            f.write(f'taUserID,duration,classID\n')

    hist = pd.read_csv(histfile)
    return hist

#
# add a meeting to the history csv
#
def add_meeting(ta):
    with open(histfile, 'a') as f:
        f.write(f'{ta.get_ta_id()},{ta.get_last_meeting_duration()},{ta.get_class_id()}\n') 



#
# drop meetings from file
#
def delete_meeting(index):
    if (index == -1):
        return False 
    index = index + 1
    i = 0
    f = open(histfile, 'r')
    rows = f.readlines()
    with open(histfile, 'w') as f:
        for row in rows:
            if (i != index):
                f.write(row)
                print(row)
            i += 1

#
# get average meeting time
#
def avg_meeting_time(class_id):
    hist = read_history()
    section = hist[hist['classID'] == class_id]
    avg_time = section['duration'].mean()

    return avg_time


