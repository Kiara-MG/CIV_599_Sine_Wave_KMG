# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:17:38 2024

@author: Kiara-MG
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters for the plot
amp = 1 # Amplitude of the wave, using 1 as a default
freq = 1 # Cycles/second
rate = 100 # Number of samples per second
dur = 5 # Total duration of the plot
noise_scale = 0.2 # Note: Chose a 0.2 scale for clarity on plot, but it is arbritrary

# Create a time array for the duration of the plot
time = np.linspace(0, dur, int(dur * rate))

# Calculate the sine wave values for each time value. It is currently set so that
# every cycle of the sine wave is 1 second long
sine_wave = amp * np.sin(2 * np.pi * freq * time)

# Create random noise for the time array
random_noise = np.random.normal(scale=noise_scale, size=(dur * rate))

# Superimpose sine_wave and noise
superimposed = sine_wave + random_noise

# Plot the sine wave
plt.plot(time, random_noise, label='Random Noise')
plt.plot(time, superimposed, label='Superimposed')
#Plotted sine wave last for better clarity
plt.plot(time, sine_wave, label='Sine Wave')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.title('Sine Wave Generator')
plt.legend()
plt.show()