import pandas as pd

#Convert CSV to HTML to load into Data page
gitdf = pd.read_csv("cities.csv")
df.to_html('data.html', index=False)
table = df.to_html()
print(table)
