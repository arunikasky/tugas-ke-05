import numpy as np
import matplotlib.pyplot as plt

t0 = 0          #waktu awal
tn = 450       # dalam waktu berapa hari
ndata = 2500    #jumlah data

t = np.linspace(t0, tn, ndata)
h = t[2] - t[1]

N = 2500    #Jumlah Populasi
I0 = 25      #Jumlah awal terinfeksi
R0 = 3      #Jumlah awal sembuh
S0 = N - I0 - R0 # Jumlah awal rentan

I = np.zeros(ndata)
S = np.zeros(ndata)
R = np.zeros(ndata)

I[0] = I0
S[0] = S0
R[0] = R0

beta = 0.7  #Laju penularan
gamma = 0.15 #Laju pemulihan

for n in range(0, ndata-1):
    S[n+1] = S[n] - h*beta/N*S[n]*I[n]
    I[n+1] = I[n] + h*beta/N*S[n]*I[n] - h*gamma*I[n]
    R[n+1] = R[n] + h*gamma*I[n]

plt.plot(t,S, label = 'S')
plt.plot(t,I, label = 'I')
plt.plot(t,R, label = 'R')
plt.legend()
plt.show()
