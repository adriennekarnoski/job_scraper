"""Functions to chart different information from csv files."""

import numpy as np
import matplotlib.pyplot as plt
from app import get_weekdays, state_counter, time_counter, tag_counter


def chart_states(data):
    """Function to chart state count on bar graph."""
    states = list(data.keys())
    y_pos = np.arange(len(states))
    count = list(data.values())
    plt.bar(y_pos, count, align='center', alpha=0.5)
    plt.xticks(y_pos, states)
    plt.ylabel('Number of Posts')
    plt.title('Number of Posts Per State')
    plt.show()


def chart_days(data):
    """Function to chart the number of posts over the previous week."""
    time_dict, now = data[0], data[1]
    days = list(time_dict.keys())
    count = list(time_dict.values())
    plt.plot(days, count)
    x = np.arange(8)
    week_list = get_weekdays(now)
    plt.ylabel('Posts')
    plt.title('Post Frequency')
    plt.xticks(x, week_list)
    plt.show()


def chart_tags(data):
    """Function to chart tag count on bar graph."""
    tags = data[0]
    y_pos = np.arange(len(tags))
    count = data[1]
    plt.bar(y_pos, count, align='center', alpha=0.5)
    plt.xticks(y_pos, tags)
    plt.ylabel('Number of Posts')
    plt.title('Top 10 Tags')
    plt.show()

if __name__ == '__main__':
    # chart_states(state_counter())
    chart_tags(tag_counter())