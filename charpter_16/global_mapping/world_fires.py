import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/Southern_Africa_7d.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
   
    lat_ind = header_row.index('latitude')    
    lon_ind = header_row.index('longitude')
    brit_ind = header_row.index('brightness')

    lons, lats, brights = [], [], []
    for row in reader:
        lon = float(row[lon_ind])
        lat = float(row[lat_ind])
        bright = float(row[brit_ind])
        lons.append(lon)
        lats.append(lat)
        brights.append(bright)

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [brit//80 for brit in brights],
        'color': brights,
        'colorscale': 'Jet',
        'reversescale': False,
        'colorbar': {'title': 'Brightness'},
    },
}]    

my_layout = Layout(title='World Fires')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')