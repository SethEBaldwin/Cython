import pivot
import pandas as pd
import numpy as np
import time

N_ROWS = 1000000
N_COLS = 100
N_IDX = 10000

NAME_IDX = 'to_be_idx'
NAME_COL = 'to_be_col'
NAME_VALUE = 'value'

def gen_df():
    col1 = ['idx{}'.format(x) for x in np.random.randint(0, N_IDX, size=N_ROWS)]
    col2 = ['col{}'.format(x) for x in np.random.randint(0, N_COLS, size=N_ROWS)]
    col3 = [x for x in np.random.normal(size=N_ROWS)]

    data = np.transpose([col1, col2, col3])
    df = pd.DataFrame(data, columns=[NAME_IDX, NAME_COL, NAME_VALUE], index=range(len(data)))
    df[NAME_VALUE] = df[NAME_VALUE].astype(np.float64)

    #print(df)

    return df

def test_pivot_orig():

    df = gen_df()

    # time

    msg = 'cython'
    tick = time.perf_counter()
    pivot_cython = pivot.pivot(df, index=NAME_IDX, column=NAME_COL, value=NAME_VALUE, agg='orig')
    print(msg, time.perf_counter() - tick)
    #print(pivot_cython)

    msg = 'pandas'
    tick = time.perf_counter()
    pivot_pandas = df.pivot_table(index=NAME_IDX, columns=[NAME_COL], values=NAME_VALUE, fill_value=0.0, aggfunc='sum')
    print(msg, time.perf_counter() - tick)
    #print(pivot_pandas)

    # check results are equal

    is_equal = (pivot_cython.to_numpy() == pivot_pandas.to_numpy()).all()
    print('componentwise equal: ', is_equal)
    epsilon = 1e-8
    within_epsilon = (np.absolute(pivot_cython.to_numpy() - pivot_pandas.to_numpy()) < epsilon).all()
    print('componentwise within {} :'.format(epsilon), within_epsilon)

    assert is_equal
    assert within_epsilon

def test_pivot_sum():

    df = gen_df()

    # time

    msg = 'cython'
    tick = time.perf_counter()
    pivot_cython = pivot.pivot(df, index=NAME_IDX, column=NAME_COL, value=NAME_VALUE, agg='sum')
    print(msg, time.perf_counter() - tick)
    #print(pivot_cython)

    msg = 'pandas'
    tick = time.perf_counter()
    pivot_pandas = df.pivot_table(index=NAME_IDX, columns=[NAME_COL], values=NAME_VALUE, fill_value=0.0, aggfunc='sum')
    print(msg, time.perf_counter() - tick)
    #print(pivot_pandas)

    # check results are equal

    is_equal = (pivot_cython.to_numpy() == pivot_pandas.to_numpy()).all()
    print('componentwise equal: ', is_equal)
    epsilon = 1e-8
    within_epsilon = (np.absolute(pivot_cython.to_numpy() - pivot_pandas.to_numpy()) < epsilon).all()
    print('componentwise within {} :'.format(epsilon), within_epsilon)

    assert is_equal
    assert within_epsilon

def test_pivot_mean():

    df = gen_df()

    # time

    msg = 'cython'
    tick = time.perf_counter()
    pivot_cython = pivot.pivot(df, index=NAME_IDX, column=NAME_COL, value=NAME_VALUE, agg='mean')
    print(msg, time.perf_counter() - tick)
    #print(pivot_cython)

    msg = 'pandas'
    tick = time.perf_counter()
    pivot_pandas = df.pivot_table(index=NAME_IDX, columns=[NAME_COL], values=NAME_VALUE, fill_value=0.0, aggfunc='mean')
    print(msg, time.perf_counter() - tick)
    #print(pivot_pandas)

    # check results are equal

    is_equal = (pivot_cython.to_numpy() == pivot_pandas.to_numpy()).all()
    print('componentwise equal: ', is_equal)
    epsilon = 1e-8
    within_epsilon = (np.absolute(pivot_cython.to_numpy() - pivot_pandas.to_numpy()) < epsilon).all()
    print('componentwise within {} :'.format(epsilon), within_epsilon)

    assert is_equal
    assert within_epsilon