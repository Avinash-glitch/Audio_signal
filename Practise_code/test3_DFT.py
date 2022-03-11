import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import get_window
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "D:\Projects\sms-tools-master\sms-tools-master\software\models"))
import utilFunctions as UF
import dftModel as DFT

"""
    inputFile: input sound file (monophonic with sampling rate of 44100)
    window: analysis window type (choice of rectangular, hanning, hamming, blackman, blackmanharris)
    M: analysis window size (odd integer value)
    N: fft size (power of two, bigger or equal than than M)
    time: time  to start analysis (in seconds)
"""
window = "hamming"
M = 511
N = 1024
time = .2
# read input sound (monophonic with sampling rate of 44100)
fs, x = UF.wavread("D:\Projects\sms-tools-master\sms-tools-master\sounds\oboe-A4.wav")
# compute analysis window
w = get_window(window, M)
x1 = x[:M]
(mX, pX) = DFT.dftAnal(x1, w, N)
mX1=mX.copy()
mX1[:50]= 20 * np.log10(0.1)
y = DFT.dftSynth(mX, pX, M) 
y2 = DFT.dftSynth(mX1, pX, M)
