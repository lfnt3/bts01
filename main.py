import pandas as pd
import numpy as np
import functions as fc

N = 1000
df2 = pd.DataFrame({'A': range(1, N + 1, 1)})
df2['B'] = df2['A']*2
# print(df2)

ndarray1 = fc.make_ndarray_from_dataframe(df2, ['A', 'B'])
# print(ndarray1)