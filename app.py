import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from thz_utils import generate_thz_pulse, fresnel_transmission

st.set_page_config(page_title="THz Pulse Propagation Simulator", layout="wide")

st.title("🌐 THz Pulse Propagation Through a Material")

# --- User Inputs ---
st.sidebar.header("Simulation Parameters")
n_material = st.sidebar.slider("Refractive Index (n)", 1.0, 5.0, 3.0, 0.1)
thickness = st.sidebar.slider("Material Thickness (µm)", 1.0, 200.0, 50.0, 1.0)
pulse_width = st.sidebar.slider("Pulse Width (ps)", 0.2, 2.0, 0.5, 0.1)
center_freq = st.sidebar.slider("Center Frequency (THz)", 0.5, 3.0, 1.0, 0.1)

# --- Generate and Propagate Pulse ---
t, E0 = generate_thz_pulse(pulse_width, center_freq)
E_transmitted = fresnel_transmission(E0, n_material, thickness, t)

# --- Plotting ---
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].plot(t, E0, label="Incident Pulse")
ax[0].plot(t, E_transmitted, label="Transmitted Pulse")
ax[0].set_xlabel("Time (ps)")
ax[0].set_ylabel("Electric Field")
ax[0].legend()
ax[0].set_title("Time Domain")

freq = np.fft.fftfreq(len(t), d=(t[1] - t[0]))
E0_fft = np.abs(np.fft.fft(E0))
Et_fft = np.abs(np.fft.fft(E_transmitted))

ax[1].plot(freq, E0_fft, label="Incident")
ax[1].plot(freq, Et_fft, label="Transmitted")
ax[1].set_xlim(0, 4)
ax[1].set_xlabel("Frequency (THz)")
ax[1].set_ylabel("Amplitude")
ax[1].set_title("Frequency Domain")
ax[1].legend()

st.pyplot(fig)
