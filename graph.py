import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from app import get_weekdays, state_counter, time_counter

def make_pdf(date):
    """."""
    pp = PdfPages('multipage.pdf')
    plt.savefig(pp, format='pdf')
    pp.close()


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
    """."""
    time_dict, now = data[0], data[1]
    days = list(time_dict.keys())
    count = list(time_dict.values())

    plt.plot(days, count)

    plt.ylabel('Posts')


    plt.title('Post Frequency')
    x = np.arange(8)
    week_list = get_weekdays(now)
    plt.xticks(x, week_list)

    plt.show()

if __name__ == '__main__':
    # chart_states(state_counter())
    chart_days(time_counter())