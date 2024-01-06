import gtsam
from gtsam import DiscreteDistribution
import gtbook
from gtbook.discrete import Variables
from gtbook.display import show

VARIABLES = Variables()
def pretty(obj):
    return gtbook.display.pretty(obj, VARIABLES)