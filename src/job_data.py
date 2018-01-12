"""File for graphing information from CSV file."""
from csv import reader
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from collections import Counter


class JobData(object):
    """."""

    def __init__(self, environment=None):
        """."""
        self.col_names = ['date', 'link', 'title', 'posted', 'company', 'location', 'tags']
        if environment == 'test':
            self.environment = 'test'
            self.df = pd.read_csv('src/sample_jobs.csv', delimiter='$', names=self.col_names, header=None)
        if environment is None:
            self.environment = 'live'
            self.df = pd.read_csv('jobs.csv', delimiter='$', names=self.col_names, header=None)
        self.date = None
        self.state_dict = None
        self.time_dict = None
        self.top_ten = None

    def count_states(self):
        """Function to count instances of states."""
        state_list = []
        for item in df['location']:
            index = item.find(',')
            state = str(item[index + 2:])
            state_list.append(state)
        self.state_dict = dict(Counter(state_list))
        return state_dict

    def chart_states(self):
        """Function to chart state count on bar graph."""
        if self.state_dict:
            states = list(data.keys())
            y_pos = np.arange(len(states))
            count = list(data.values())
            plt.bar(y_pos, count, align='center', alpha=0.5)
            plt.xticks(y_pos, states)
            plt.ylabel('Number of Posts')
            plt.title('Number of Posts Per State')
            plt.show()
        else:
            raise ValueError('No states to chart.')

    def count_days(self):
        """Function to organize times of posts."""
        self.time_dict = {}
        for i in range(8):
            self.time_dict[str(i)] = 0
        self.now = self.df['date'][0]
        for item in self.df['posted']:
            if item == 'yesterday':
                self.time_dict['1'] += 1
            index = item.find(' ago')
            time = item[:index]
            if time[-1] == 'h':
                hours = time.replace("h", "")
                get_date = self.now - datetime.timedelta(hours=int(hours))
                if now.date() == get_date.date():
                    self.time_dict['0'] += 1
                self.time_dict['1'] += 1
            if time[-1] == 'd':
                days = time.replace("d", "")
                self.time_dict[days] += 1
            if time[-1] == 'w':
                self.time_dict['7'] += 1
        return self.time_dict

        def chart_days(self):
            """Function to chart the number of posts over the previous week."""
            if self.time_dict:
                days = list(self.time_dict.keys())
                count = list(self.time_dict.values())
                plt.plot(days, count)
                x = np.arange(8)
                week_list = self._get_weekdays(now)
                plt.ylabel('Posts')
                plt.title('Post Frequency')
                plt.xticks(x, week_list)
                plt.show()
            else:
                raise ValueError('No days available')

        def _get_weekdays(self):
            """Function to get day of the week and create list accordingly."""
            days = ['Sunday',
                    'Saturday',
                    'Friday',
                    'Thursday',
                    'Wednesday',
                    'Tuesday',
                    'Monday']
            weekday = self.date.weekday()
            if weekday == 0:
                week = days[:]
            else:
                week = days[weekday:] + days[:weekday]
            week[0] = 'Today'
            week.append('One Week')
            return week

        def tag_counter(self):
            """Function to return top ten tags for all posts."""
            tag_list = []
            tag_count = []
            for item in self.df['tags']:
                to_list = [x.strip() for x in item.split(',')]
                filter_list = list(filter(None, to_list))
                tag_list = tag_list + filter_list
            tag_dict = dict(Counter(tag_list))
            tag_names = sorted(tag_dict, key=tag_dict.get, reverse=True)[:10]
            for item in tag_names:
                tag_count.append(tag_dict[item])
            self.top_ten = dict(zip(tag_names, tag_count))
            return top_ten

        def chart_tags(self):
            """Function to chart tag count on bar graph."""
            if self.top_ten:
                count = list(self.top_ten.values())
                tags = list(self.top_ten.keys())
                y_pos = np.arange(len(tags))
                count = data[1]
                plt.bar(y_pos, count, align='center', alpha=0.5)
                plt.xticks(y_pos, tags)
                plt.ylabel('Number of Posts')
                plt.title('Top 10 Tags')
                plt.show()
            else:
                raise ValueError('Top Ten not available')

# if __name__ == '__main__':
#     state_counter()
