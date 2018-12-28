import pandas as pd
import numpy as np
import functions as fc

# N = 1000
# df = pd.DataFrame({'feature_1': range(1, N + 1, 1),
#                     'feature_2': range(1, N + 1, 1)
#                     })
# df['labels'] = df['feature_1']*2
# print(df)
#
# df.to_csv(f'./source/df.csv', header=True, index=False)

# ndarray1 = fc.make_ndarray_from_dataframe(df, ['feature_1', 'feature_2', 'labels'])
# print(ndarray1)


# a = np.random.randint(1, 100, size=(1000, 1))
# print(a)

# df = pd.DataFrame({'feature_1': a[0]})

df2 = pd.DataFrame({'feature_1': np.random.randint(1, 20, size=(10000, 1)[0]),
                   'feature_2': 10
                   })
df2['labels'] = np.where((df2['feature_1'] == df2['feature_2']), 1, 0)
print(df2)

df2.to_csv(f'./source/df2.csv', header=True, index=False)