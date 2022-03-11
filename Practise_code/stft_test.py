import numpy as np
import matplotlib.pyplot as plt
import os, sys
from scipy.signal import get_window
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "D:\Projects\sms-tools-master\sms-tools-master\software\models"))
import utilFunctions as UF
import stft as STFT
from stft import stftAnal
import stft_function 

inputfile = "D:\Projects\sms-tools-master\sms-tools-master\sounds\cello-double.wav"
fs,x = UF.wavread(inputfile)
window = 'hamming'
M=801
N=1024
H=400
w= get_window(window,M)
#mX,pX=STFT.stftAnal(x,w,N,H)


