"""File for graphing information from CSV file."""
from csv import reader
import pandas as pd
import plotly
import plotly.graph_objs


# with open('jobs.csv', 'r') as f:
#     data = list(reader(f))
#     print(data[0])

# pyplot.plot(range(len(temp)), temp)
# pyplot.show()

col_names = ['link', 'title', 'posted', 'company', 'location', 'tags']
df = pd.read_csv('jobs.csv', delimiter='$', names=col_names, header=None)




plotly.offline.plot({"data": [
    plotly.graph_objs.Bar(x=['food', 'service', 'environment'], y=[3.4, 4.2, 4.3])
]
})

def state_counter():
    """."""
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
    return state_list, state_dict



if __name__ == '__main__':
    state_counter()