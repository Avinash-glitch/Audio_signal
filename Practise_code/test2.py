from stat import UF_APPEND
import numpy as np
from scipy.signal import triang
from scipy.fftpack import fft
import sys,os,math
#sys.path.append(os.path.join(os.path.dirname(os.path.realpath(_file_)), 'D:\Projects\sms-tools-master\sms-tools-master\software\models' ))
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'D:\Projects\sms-tools-master\sms-tools-master\software\models'))
import utilFunctions as UF

M = 501

#find the center of the sample
hM1 = int(math.floor((M+1)/2))
hM2 = int(math.floor(M/2))
(fs,x) = UF.wavread("D:\Projects\sms-tools-master\sms-tools-master\sounds\soprano-E4.wav")
x1 = x[5000:5000+M] * np.hamming(M)

N = 500
fftbuffer= np.zeros(N)
fftbuffer[:hM1]= x1[hM2:]
fftbuffer[N-hM2:]= x1[:hM2]
X= fft(fftbuffer)
#X= fft(x)
#mx = 20* np.log10(abs(X))
mx = abs(X)
px= np.unwrap(np.angle(X))

