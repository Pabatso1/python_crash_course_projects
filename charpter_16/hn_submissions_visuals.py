from operator import itemgetter

import requests
from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    except KeyError:
        # This is a special YC post with comments dissabled.
        continue
    else:    
        submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), 
                            reverse=True)    

labels, comments, texts = [], [], []
for submission_dict in submission_dicts:
    repo_name = submission_dict['title']
    repo_link = submission_dict['hn_link']
    comment = submission_dict['comments']
    label = f"<a href='{repo_link}'>{repo_name}<a/>"
    comments.append(comment)
    labels.append(label)
    texts.append(repo_name)

data = [{
    'type': 'bar',
    'x': labels,
    'y': comments,
    'hovertext': texts,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6
}]

my_layout = {
    'title': "Most popular articles on Hacker-News",
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Articles',
        'titlefont': {'size': 24},
        'tickfont': {'size':14},
    },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hacker-news_articles.html')