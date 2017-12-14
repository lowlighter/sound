# Liste des dépendances
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.ticker as ticker
import scipy.io.wavfile as sw
import itertools
import math
import re
import sys
import IPython.display as ipd
from scipy import signal
from scipy.signal import butter, lfilter, firwin
from operator import add
from matplotlib.widgets import Slider
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix, precision_score
from ipywidgets import FloatProgress
from IPython.display import display
