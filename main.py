import pandas as pd
import numpy as np
import functions as fc

N = 1000
df = pd.DataFrame({'feature_1': range(1, N + 1, 1),
                    'feature_2': range(1, N + 1, 1)
                    })
df['labels'] = df['feature_1']*2
print(df)

df.to_csv(f'./source/df.csv', header=True, index=False)

ndarray1 = fc.make_ndarray_from_dataframe(df, ['feature_1', 'feature_2', 'labels'])
print(ndarray1)