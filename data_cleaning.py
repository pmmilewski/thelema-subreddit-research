# Imported data is in form of list of responses containig all links in subreddit
# links: data[]["data"]["children"]
import json
import pandas as pd

with open('data.json') as data_file:
    raw_data = json.load(data_file)

#Interesting fields: author, created_utc, id, title, ups, downs, score
# domain, num_comments, over_18, type (t3)

cols = ["id", "created_utc", "author", "title", "ups", "downs", "score",
"num_comments", "over_18"  ]

d = {"id": list(), "created_utc": list(), "author": list(), "title": list(),
 "ups": list(), "downs": list(), "score": list(),"num_comments": list(), "over_18": list()}

for part in raw_data:
    for child in part["data"]["children"]:
        for col in cols:
            if col == "created_utc":
                d[col].append(pd.to_datetime(child["data"][col], unit="s"))
            else:
                d[col].append(child["data"][col])

data = pd.DataFrame.from_dict(d)
data.to_csv("links.csv")
