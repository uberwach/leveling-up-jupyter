import pandas as pd

# Set Pandas display options for easier reading
pd.set_option("max_colwidth", 100)
pd.set_option("display.max_rows", 1000)
pd.set_option("display.max_columns", 9001)  # there is a scrollbar and '...' just looks stupid
pd.set_option('display.float_format', lambda x: '{:,.2f}'.format(x))
