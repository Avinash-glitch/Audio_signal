import os
import sys
import numpy as np
import math
from scipy.signal import get_window,resample
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "D:\Projects\sms-tools-master\sms-tools-master\software\models"))
import utilFunctions as UF
import stochasticModel as SCM
(fs,x) = UF.wavread("D:\Projects\sms-tools-master\sms-tools-master\sounds\ocean.wav")
H = 256
#hN = int(N/2)
scf = 0.2
w=get_window('hamming',M)
x1= x[10000 : 10000+M] * w
X = fft(x1)
mX = 20*np.log10(abs(X[:hN]))
mXenv = resample(np.maximum(-200,mX), int(hN*scf))

mY = resample(mXenv,hN)
pY = 2*np.pi*np.random.rand(hN)
Y = np.zeros(N)
Y[:hN]= 10**(mY/20) * np.exp(1j * pY)
Y[hN+1:]= 10**(mY[:0:-1]/20) * np.exp(-1j * pY[:0:-1])
y=np.real(ifft(Y))
mXenv= SCM.stochasticModelAnal(x,H,H*2,scf)