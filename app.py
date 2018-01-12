"""File for graphing information from CSV file."""
from csv import reader
import pandas as pd
import plotly
import plotly.graph_objs
import datetime
from collections import Counter

col_names = ['date', 'link', 'title', 'posted', 'company', 'location', 'tags']
df = pd.read_csv('jobs.csv', delimiter='$', names=col_names, header=None)


def state_counter():
    """Function to count instances of states."""
    state_list = []
    for item in df['location']:
        index = item.find(',')
        state = str(item[index + 2:])
        state_list.append(state)
    state_dict = dict(Counter(state_list))
    return state_dict


def time_counter():
    """Function to organize times of posts."""
    time_dict = {}
    for i in range(8):
        time_dict[str(i)] = 0
    now = df['date'][0]
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
    days = ['Sunday',
            'Saturday',
            'Friday',
            'Thursday',
            'Wednesday',
            'Tuesday',
            'Monday']
    weekday = data.weekday()
    if weekday == 0:
        week = days[:]
    else:
        week = days[weekday:] + days[:weekday]
    week[0] = 'Today'
    week.append('One Week')
    return week


def tag_counter():
    """Function to return top ten tags for all posts."""
    tag_list = []
    tag_count = []
    for item in df['tags']:
        to_list = [x.strip() for x in item.split(',')]
        filter_list = list(filter(None, to_list))
        tag_list = tag_list + filter_list
    tag_dict = dict(Counter(tag_list))
    top_ten = sorted(tag_dict, key=tag_dict.get, reverse=True)[:10]
    for item in top_ten:
        tag_count.append(tag_dict[item])
    return top_ten, tag_count

# if __name__ == '__main__':
#     state_counter()
