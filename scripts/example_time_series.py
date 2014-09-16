import matplotlib
matplotlib.use('TKAgg')

import matplotlib.pyplot as plt
import numpy as np


from turbulence_jens import Turbulence



target_max_frequency = 5000.0 # Max valid frequency in Hz
duration = 100.0 # Duration of the signal

fs = 2.0 * target_max_frequency

samples = int(duration * fs)


c = 343.0
mean_mu_squared = 3.0e-6
distance = 2000.0
f0 = 200.0
L = 12.0

t = np.arange(samples) / fs

x = np.sin(2.0*np.pi*f0*t)

spacing = np.zeros(samples)
turbulence = Turbulence(spacing, c, target_max_frequency, mean_mu_squared, distance, f0, L, samples, saturation=True)
turbulence.randomize().generate()
y = turbulence.apply_single_modulation(x)

from acoustics.standards.iec_61672_1_2013 import fast

fig = plt.figure()

ax0 = fig.add_subplot(211)
ax0.plot(t, x, linestyle='-', label='$x(t)$')
ax0.plot(t, y, linestyle='--', label='$y(t)$')
ax0.set_title("Instantaneous pressure $p(t)$")
ax0.set_xlim(0.0, f0/fs)
ax0.set_xlabel('$t$ in s')
ax0.set_ylabel('$p$ in Pa')
ax0.grid()
ax0.legend()
#ax0.set_ylim(

ax1 = fig.add_subplot(212)
ax1.plot(*fast(x, fs), linestyle='-', label='$x(t)$')
ax1.plot(*fast(y, fs), linestyle='--', label='$y(t)$')
ax1.set_title("Sound pressure level $L_{p,F}$")
ax1.set_xlabel('$t$ in s')
ax1.set_ylabel('$L_{p,F}$ in dB re. 1 Pa')
ax1.legend()
ax1.grid()
fig.tight_layout()
fig.savefig("../figures/time_signal.png")

_, L = fast(y,fs)
print(L.std())


