import numpy as np

def generate_thz_pulse(pulse_width_ps, center_freq_thz, t_range_ps=10.0, dt=0.01):
    t = np.arange(-t_range_ps, t_range_ps, dt)
    envelope = np.exp(-t**2 / (2 * pulse_width_ps**2))
    carrier = np.cos(2 * np.pi * center_freq_thz * t)
    E = envelope * carrier
    return t, E

def fresnel_transmission(E, n, d_um, t, c=299.792):  # c in µm/ps
    # Simple delay based on thickness and n
    delay_ps = 2 * n * d_um / c  # 2 for roundtrip if reflective
    E_shifted = np.interp(t, t - delay_ps, E, left=0, right=0)
    T = 2 / (1 + n)  # Fresnel transmission coefficient
    return T * E_shifted
