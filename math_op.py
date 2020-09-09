"""
Basic math operations
"""
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class MathOp():

    @classmethod
    def __init__(cls,series,default_col):
        cls.series = series
        cls.default_col=default_col

    @classmethod
    def local_extremum(cls,start_point,end_point,window = 6,min_= 'min',max_='max' ):
        """

        Purpose
        -------
        Function to find local extremum (min and max) on stock price on a ran, we check current price versus past and future price.


        Parameters
        ----------
        window : the number of the data we check before and after to determine the  local extremum.
                window by default is 6


        Returns
        ------
        Return a pandas dataframe with not empty min or max value (if both are empty, not return. If one of
        them has a value, return the local min or max with index no)
        """

        cls.series=cls.series.loc[start_point:end_point,cls.default_col]
        cls.series=pd.DataFrame({cls.default_col: cls.series})

        cls.series[min_] = cls.series.iloc[argrelextrema(cls.series.values, np.less_equal,
                                                          order=window)[0]][cls.default_col]
        cls.series[max_] = cls.series.iloc[argrelextrema(cls.series.values, np.greater_equal,
                                                          order=window)[0]][cls.default_col]

        # Plot results - to get ride when finished
        """ 
        plt.scatter(cls.series.index, cls.series[min_], c='r')
        plt.scatter(cls.series.index, cls.series[max_], c='g')
        plt.plot(cls.series.index, cls.series[cls.default_col])
        plt.show()
        """

        #Filter nan value for min or max out
        cls.series=cls.series.loc[(cls.series[min_].isna())==False | (cls.series[max_].isna() == False)]

        return cls.series