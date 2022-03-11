import os
import sys
from tkinter import N
import numpy as np
from scipy.signal import get_window,blackmanharris,triang
import matplotlib.pyplot as plt
import math
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),"D:\Projects\sms-tools-master\sms-tools-master\software\models"))
import stft
import dftModel as DFT
import matplotlib.pyplot as plt
import utilFunctions as UF
from scipy.fftpack import fft,ifft

bins=np.array([-4,-3,-2,-1,0,1,2,3]) + .5
X = UF.genBhLobe(bins)

fs,x= UF.wavread("D:\Projects\sms-tools-master\sms-tools-master\sounds\oboe-A4.wav")
M = 511 
N=512
hN = int(N/2)
H = int(N/4)
t=-70
w=get_window('hamming',M)
u = int(0.8*fs)
x1 = x[u : u + M]
mx,px = DFT.dftAnal(x1,w,N)
ploc = UF.peakDetection(mx,t)
iploc,imag,iphase = UF.peakInterp(mx,px,ploc)
ifreq = fs * iploc/float(N)
Y = UF.genSpecSines(ifreq, imag, iphase, N, fs)
y= np.real(ifft(Y))


#converting blackman-harris to traingular
sw=np.zeros(N)
ow= triang(N/2)
sw[hN-H:hN+H]= ow
bh = blackmanharris(N)
bh= bh/sum(bh) #normlaize window
sw[hN-H :hN +H] = sw[hN-H :hN +H] / bh[hN-H :hN +H] 
yw= np.zeros(N)
yw[:hN-1] = y[hN+1:]
yw[hN-1:] = y[:hN+1]
yw *=sw

freqaxis = fs* np.arange((N/2)+1)/float(N)
plt.plot(freqaxis,mx)
plt.plot(fs * iploc /N , imag,marker='x',linestyle ='')
plt.show()