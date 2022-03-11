
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import get_window,resample
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "D:\Projects\sms-tools-master\sms-tools-master\software\models"))
import utilFunctions as UF
import dftModel as DFT

fs, x2 = UF.wavread("D:\Projects\sms-tools-master\sms-tools-master\sounds\soprano-E4.wav")
fs1, x1 = UF.wavread("D:\Projects\sms-tools-master\sms-tools-master\sounds\ocean.wav")
M=N=512
w= get_window('hanning',M)
xw1 = x1[10000:10000 + M] * w
xw2 = x2[10000:10000 + M] * w
mX1,pX1 = DFT.dftAnal(xw1,w,N)
mX2,pX2 = DFT.dftAnal(xw2,w,N)
smoothf = 0.2
mX2smooth1 = resample(np.maximum(-200,mX2),int(mX2.size * smoothf))
mX2smooth2 = resample(mX2smooth1,int(N/2))
balancef = 0.7
mY = balancef * mX1 + (1-balancef) *mX2smooth2
y= DFT.dftSynth(mY,pX1,N) * sum(w)

