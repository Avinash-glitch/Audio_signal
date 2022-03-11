
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import get_window
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "D:\Projects\sms-tools-master\sms-tools-master\software\models"))
import utilFunctions as UF
import dftModel as DFT

fs, x = UF.wavread("D:\Projects\sms-tools-master\sms-tools-master\sounds\oboe-A4.wav")
M=N=512
w= get_window('hanning',M)
xw = x[10000:10000 + M] * w
mX,pX = DFT.dftAnal(xw,w,N)
filter = get_window('hamming',30) * -60
center_bin=40

mY=np.copy(mX)
mY[center_bin -15:center_bin+15]= mX[center_bin-15:center_bin +15] + filter
y= DFT.dftSynth(mY,pX,N) * sum(w)