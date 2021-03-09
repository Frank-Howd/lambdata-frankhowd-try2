# Imports
import numpy as np
import pandas as pd

from sklearn.utils import shuffle

# Test Data
test_df = pd.DataFrame({'column 0': [np.NaN, 4, 3, 1, 4, 2, 1, 5, 5, 2],
                        'column 1': [9, 1, 2, 3, 4, np.NaN, np.NaN, 0, 22, 1],
                        'column 2': [10, 2, 2, 100, 1, 2, 4, 3, 1, 2],
                        'column 3': [np.NaN, np.NaN, np.NaN, 44, 4, 5, 6, 2, 43, 2],
                        'column 4': [5, 6, 7, 7, 3, 2, 5, 2, 4, 4],
                        'column 5': [7, 8, 4, 2, 5, 6, 7, 3, 5, 6],
                        'column 6': [45, 243, 5, 1, 4, 2, 3, 5, 66, 5],
                        'column 7': [1, 2, np.NaN, 3, 5, 77, 88, 99, 2, 4],
                        'column 8': [np.NaN, 54, 23, 1, 33, 55, 22, 1, 3, 4],
                        'column 9': [3, 22, 11, 4, 5, 4, 3, 2, 1, 4],
                        'column 10': [45, 33, 23, 1, 44, 33, 234, 234, 111, 3]})
print(test_df)
test_df.head()


addy_series = pd.Series({0: '890 Jennifer Brooks\nNorth Janet, WY 24785',
                         1: '8394 Kim Meadow\nDarrenville, AK 27389',
                         2: '379 Cain Plaza\nJosephburgh, WY 06332',
                         3: '5303 Tina Hill\nAudreychester, VA 97036'})

print(addy_series)


# 1
def null_count(df):
    """Check a DataFrame for null values and returns the number of missing values"""
    return df.isna().sum().sum()


def null_count_alt(df):
    """Check a Dataframe for null values and returns the number of missing values"""
    x = [test_df[col].isna().sum() for col in test_df.columns]
    y = 0
    for _ in x:
        y += _
    return y


# 1 Tests
# print("null_count:", null_count(test_df), end=' ')
# print("null_count_alt:", null_count_alt(test_df))


# 2
def train_test_split(df, frac):
    """Create a train/test split function for a data frame that returns both the
    training and test sets.  'frac' refers to the percent of data you would like
    to set aside for training"""
    cutoff = df.index < int(df.shape[0] * frac)
    df_train = df.loc[cutoff]
    df_test = df.loc[~cutoff]
    return df_train, df_test


# 2 Tests
# df1, df2 = train_test_split(test_df, 0.6)
# assert isinstance(df1, pd.DataFrame)
# assert isinstance(df2, pd.DataFrame)
# print(df1, '\n\n')
# print(df2)


# 3
def randomize(df, seed=None):
    """Develop a randomization function that randomizes all of a dataframe's cells
    then returns that randomized dataframe.  This function also accepts a random
    seed for reproducible randomization"""
    df = df.copy()
    columns = df.columns
    df = shuffle(df[columns], random_state=seed)
    return df


# 3 Tests
# print(randomize(test_df, seed=22))


# 4
def addy_split(addy_series):
    """Split addresses into three columns (df['city'], df['state'], df['zip']"""
    cities = []
    states = []
    zips = []
    for addy in addy_series:
        split_addy_1 = (addy.split(','))
        # print(split_addy_1)
        cities.append(split_addy_1[0].split('\n')[1])
        states.append(split_addy_1[1].split(' ')[1])
        zips.append(split_addy_1[1].split(' ')[2])

    df = pd.DataFrame({'city': cities,
                       'state': states,
                       'zip': zips})
    return df


# 4 Tests
print(addy_split(addy_series))

pass
