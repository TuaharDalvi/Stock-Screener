#Import the required dependency
import pandas as pd

#Read CSV file
df = pd.read_csv('Book3.csv')

#Export as HTML file
df.to_html('Book3.htm')
