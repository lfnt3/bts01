
def make_ndarray_from_dataframe(df, columns):
    ### make ndarray from pandas DataFrame to be usable with Keras
    df_copy = df.copy()
    nd_arr = df_copy.as_matrix(columns=columns)

    return nd_arr