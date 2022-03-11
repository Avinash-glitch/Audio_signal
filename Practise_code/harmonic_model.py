import numpy as np
from scipy.signal import resample, blackmanharris, triang
from scipy.fftpack import fft, ifft, fftshift
import math, copy, sys, os
from scipy.io.wavfile import write, read
from sys import platform
import matplotlib.pyplot as plt
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "D:\Projects\sms-tools-master\sms-tools-master\software\models"))
import utilFunctions as UF
import harmonicModel as HM
import sineModel as SM
import stft as STFT
import dftModel as DFT
from scipy.signal import get_window
fs,x = UF.wavread("D:\Projects\sms-tools-master\sms-tools-master\sounds\cello-double-2.wav")
M=3001
w=  get_window('blackman',M)
N= 4096
t =-70
minf0= 133
maxf0 = 300
f0et =1 
H = 1000
nH = 50
#f0= HM.f0Detection(x,fs,w,N,H,t,minf0,maxf0,foet)
xfreq,xmag,xphase = HM.harmonicModelAnal(x, fs, w, N, H, t, nH, minf0, maxf0, f0et, harmDevSlope=0.1, minSineDur=0.05)
Nframes = int(xfreq[:,0].size)
frmTime = M * np.arange(Nframes)/float(fs)
xfreq [xfreq<=0]= np. nan
plt.plot(frmTime,xfreq)
plt.show()