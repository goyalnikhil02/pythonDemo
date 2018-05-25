# import the pandas library and aliasing as pd
import pandas as pd
import numpy as np



df = pd.DataFrame(np.random.randn(8,4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# Select range of rows for all columns
print(df)
print(df.sort_index(axis=1))  