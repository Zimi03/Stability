import numpy as np
import matplotlib.pyplot as plt

def M(s):
    return s**4+12*s**3+50*s**2+84*s+45
def michaj(w):
    return ((w**4 - 50*w**2 + 45) + 1j*(-12*w**3 + 84*w))

def Nyq(w,k):
    return   (k*(w**4 - 50* w**2 + 45 + k))/((w**4 - 50* w**2 + 45 + k)**2 +(-12*w**3 + 84*w))+1j*((12*w**3 - 84*w)/((w**4 - 50* w**2 + 45 + k)**2 +(-12*w**3 + 84*w)))

w = np.linspace(0,8,1000)
Re = M(w*1j).real
Im = M(w*1j).imag
Re_n = (11/M(w*1j)).real
Im_n = (11/M(w*1j)).imag
#plt.plot(michaj(w).real, michaj(w).imag, linewidth=2,label="Wykres funkcji michajłowa")
#plt.plot(Re, Im, linestyle="--",label="sprawdzenie")
#plt.plot(Nyq(w,11).real, Nyq(w,11).imag,label="Wykres funkcji Nyquista")
plt.plot(Re_n, Im_n, linestyle="--",label="sprawdzenie")

plt.legend()
plt.grid()
plt.show()
