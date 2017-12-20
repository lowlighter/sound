# Nom
__name__ = "sound"

# Ajout du dossier dans les imports
import sys
sys.path.append("bin")

# Imports des fonctions
from adc import *
from bandpass import *
from benchmark import *
from compare import *
from compute import *
from cut import *
from drc import *
from drcz import *
from energies import *
from gen_data import *
from gen_filtered import *
from gen_filters import *
from gen_sine import *
from learning_files import *
from learning import *
from live_record import *
from player import *
from plot_avggram import *
from plot_data import *
from plot_datagram import *
from plot_dbfs import *
from plot_energies import *
from plot_filtered import *
from plot_formants import *
from plot_freqz import *
from plot_nspecgram import *
from plot_specamp import *
from plot_specgram import *
from similar import *
from similarities import *
from state_at import *
from to1D import *

# Masque les avertissements
import warnings
warnings.filterwarnings("ignore")
