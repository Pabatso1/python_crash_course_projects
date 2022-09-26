from plotly import offline
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

from random_walk import RandomWalk

rw = RandomWalk(50_000)
rw.fill_walk()

trace1 = go.Scatter(
    x=rw.x_values,
    y=rw.y_values,
    mode='markers',
    name='Random Walk',
    marker=dict(
        color=[i for i in range(len(2*rw.x_values))],
        size=2,
        colorscale='Greens',
        showscale=False
    )
)                

data = [trace1]
offline.plot(data, filename='random-walk-2d.html')