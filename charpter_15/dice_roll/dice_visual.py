from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6 and D10.
die_1 = Die()
#die_2 = Die()
 
# Make some rolls, and store the result in a list.
results = [die_1.roll() for _ in range(1000)]

# Analyze the results.
#max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(1, die_1.num_sides+1)]

# Visualize the results.
x_values = list(range(1, die_1.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title="Results of rolling two D6 1,000 times",
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')        