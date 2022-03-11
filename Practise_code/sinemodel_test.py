import os
import sys
from tkinter import N
import numpy as np
from scipy.signal import get_window
import matplotlib.pyplot as plt
import math
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),"D:\Projects\sms-tools-master\sms-tools-master\software\models"))
import stft
import dftModel as DFT
import matplotlib.pyplot as plt
import utilFunctions as UF

fs,x= UF.wavread("D:\Projects\sms-tools-master\sms-tools-master\sounds\sine-440.wav")
M = 501 
N=2048
t=-20
w=get_window('hamming',M)
u = int(0.5f*fs)
x1 = x[u : u + M]
mx,px = DFT.dftAnal(x1,w,N)
ploc = UF.peakDetection(mx,t)
iploc,imag,iphase = UF.peakInterp(mx,px,ploc)
freqaxis = fs * np.arange((N/2)+1)/float(N)
plt.plot(freqaxis,mx)
plt.plot(fs*iploc/float(N),imag,marker = 'x',linestyle= '')
plt.show()