# Create Date column from Year, Month and Day in Pandas

import pandas as pd

df = pd.DataFrame({
    'year': [2011, 2012, 2013, 2014],
    'month': [1, 2, 3, 4],
    'day': [10, 12, 14, 16],
    'champion': ['Austria', 'Belgium', 'Canada', 'Denmark']
})

print(df)

df['date'] = pd.to_datetime(
    dict(year=df.year, month=df.month, day=df.day)
)

print('-' * 50)

print(df)