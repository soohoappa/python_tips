import numpy as np
import pandas as pd
import functools

import multiprocessing as mp

def preprocessing():

    return df

def split_list(list, n_split):
    sids = np.array(list)
    np.random.shuffle(sids)
    splited_list = np.array_split(sids, n_split)
    return splited_list

def parallel_dataframe(df, unique_list, func, num_cores):
    try:
        list_split_ = split_list(unique_list, num_cores)
        pool = mp.Pool(num_cores)
        partial_pool = functools.partial(func, df)
        df = pd.concat(pool.map(partial_pool, list_split_))
        pool.close()
        pool.join()
        return df

    except (IndexError, ValueError, UnboundLocalError):
        print("Error")
        pass

def multi_processing(df, unique_list):
    # multiprocessing 
    return df

def main():
    mp.set_start_method('spawn')

    df = preprocessing()

    # extract unique list of a feature which will be applied for multiprocessing.
    unique_list = sorted(df['Student_ID'].unique())

    # multiproecssing
    df = parallel_dataframe(df, unique_list, multi_processing, mp.cpu_count())

if __name__ == '__main__':
    
    main()    