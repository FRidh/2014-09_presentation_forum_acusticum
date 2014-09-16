import matplotlib
matplotlib.use('TKAgg')

import matplotlib.pyplot as plt
import numpy as np


from turbulence_jens import Turbulence



target_max_frequency = 5000.0 # Max valid frequency in Hz
duration = 10.0 # Duration of the signal

fs = 2.0 * target_max_frequency

samples = int(duration * fs)


c = 343.0
mean_mu_squared = 3.0e-6
distance = 2000.0
f0 = 200.0
L = 12.0

spacing = np.zeros(samples)
t = Turbulence(spacing, c, target_max_frequency, mean_mu_squared, distance, f0, L, samples, saturation=True)

t.randomize().generate()
#t.plot_modulation_signal('../figures/modulations.png')

x = t.modulation_signal
t= t.times

fig = plt.figure()

ax0 = fig.add_subplot(211)
ax0.plot(t, np.abs(x), linestyle='-')
ax0.set_title("Amplitude modulation $e^{\chi (t)}$")
ax0.set_xlabel('$t$ in s')
ax0.set_ylabel('$e^{\chi}$ in Pa')
ax0.grid()
ax0.legend()

ax1 = fig.add_subplot(212)
ax1.plot(t, np.angle(x), linestyle='-')
ax1.set_title("Phase modulation $S(t)$")
ax1.set_xlabel('$t$ in s')
ax1.set_ylabel('$S$ in rad')
ax1.grid()

fig.tight_layout()
fig.savefig("../figures/modulations.png")
