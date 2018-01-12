"""File for graphing information from CSV file."""
from csv import reader
import pandas as pd
import plotly
import plotly.graph_objs
import datetime

col_names = ['link', 'title', 'posted', 'company', 'location', 'tags']
df = pd.read_csv('jobs.csv', delimiter='$', names=col_names, header=None)


def state_counter():
    """Function to count instances of states."""
    state_list = []
    state_dict = {}
    for item in df['location']:
        index = item.find(',')
        state = str(item[index + 2:])
        state_list.append(state)
    for item in state_list:
        state_dict[item] = 0
    for item in state_list:
        state_dict[item] += 1
    return state_dict


def time_counter():
    """Function to organize times of posts."""
    time_dict = {}
    for i in range(8):
        time_dict[str(i)] = 0
    now = datetime.datetime.now()
    for item in df['posted']:
        if item == 'yesterday':
            time_dict['1'] += 1
        index = item.find(' ago')
        time = item[:index]
        if time[-1] == 'h':
            hours = time.replace("h", "")
            get_date = now - datetime.timedelta(hours=int(hours))
            if now.date() == get_date.date():
                time_dict['0'] += 1
            time_dict['1'] += 1
        if time[-1] == 'd':
            days = time.replace("d", "")
            time_dict[days] += 1
        if time[-1] == 'w':
            time_dict['7'] += 1
    return [time_dict, now]


def get_weekdays(data):
    """Function to get day of the week and create list accordingly."""
    days = ['Sunday', 'Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday']
    weekday = data.weekday()
    if weekday == 0:
        week = days[:]
    else:
        week = days[weekday:] + days[:weekday]
    week[0] = 'Today'
    week.append('One Week')
    return week



if __name__ == '__main__':
    state_counter()