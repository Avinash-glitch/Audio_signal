import os
import sys
import numpy as np
import math
from scipy.signal import get_window,resample
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "D:\Projects\sms-tools-master\sms-tools-master\software\models"))
import utilFunctions as UF
import dftModel as DFT
import harmonicModel as HM

(fs,x) = UF.wavread("D:\Projects\sms-tools-master\sms-tools-master\sounds\ocean.wav")
pin = 40000
M=801
N=2048
t=-80
minf0=300
maxf0=500
f0et=5
nH =60
harmDevSlope = 0.001
stocf = 0.2

w=get_window('blackman', M)
hM1 = int(math.floor((M+1)/2))
hM2 = int(math.floor(M/2))

x1=x[pin-hM1:pin+hM2]
mX,pX = DFT.dftAnal(x1,w,N)
ploc= UF.peakDetection(mX,t)
iploc, ipmag, ipphase = UF.peakInterp(mX,pX,ploc)
ipfreq = fs *iploc/N
f0= UF.f0Twm(ipfreq,ipmag,f0et,minf0,maxf0,0)
hfreq,hmag,hphase = HM.harmonicDetection(ipfreq,ipmag,ipphase,f0,nH,[],fs,harmDevSlope)

Ns = 512
hNs= 256
Yh= UF.genSpecSines(hfreq,hmag,hphase,Ns,fs)

wr=get_window('blackmanharris',Ns)
x2=x[pin-hNs-1:pin+hNs-1] * wr/sum(wr)
fftbuffer=np.zeros(Ns)
fftbuffer[:hNs]= x2[hNs:]
fftbuffer[hNs:]=x2[:hNs]
X2 = fft(fftbuffer)
Xr = X2-Yh

mXr= 20* np.log10(abs(Xr[:hNs]))
mXenv=resample(np.maximum(-200,mXr),int(mXr.size*stocf))
stocenv=resample(mXenv,hNs)