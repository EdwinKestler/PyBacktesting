"""Module that evaluates the slope and r_square of a serie"""

from scipy import stats
from initialize import Initialize
from manip_data import ManipData as md
from init_operations import InitOp as io
import copy

class RegressionSlopeStrenght(Initialize):
    """Class that evaluates the slope and r2 value of a serie

    Take into consideration that we use r2 to see if one variable can explain movement in the other.
    We are not trying to forecast using the r2 value.

    Parameters
    ----------
    `self.sous_series` : pandas Dataframe
        Contains the subseries on which we calculate the slope and r2 value
    """

    def __init__(self,series_,self_):
        super().__init__()
        super().__call__()
        new_obj = copy.deepcopy(self_)
        self.__dict__.update(new_obj.__dict__)
        io.init_series(self)
        del new_obj, self_
        self.sous_series=md.sous_series_(series_,self.nb_data)

    def __store_stat(self):
        """Function that returns stat in a list"""

        return stats.linregress(self.sous_series[self.date_ordinal_name],
                                self.sous_series[self.default_data])

    def slope(self):
        """ Function that return the slope of a serie.
        La pente est la 1ième valeur retournée dans cette stats.linregress, d'où le [0]
        """

        return self.__store_stat()[0]

    def r_square(self):

        """
        La corrélation est la 3ième valeur retournée dans cette stats.linregress, d'où le [2]
        """

        return (self.__store_stat()[2])**2