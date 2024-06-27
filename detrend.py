from scipy.signal import detrend

# Detrend the second wave
detrended_wave = detrend(wave_with_trend)

# Apply the Butterworth high-pass filter to the second wave
filtered_wave_trend = filtfilt(b, a, wave_with_trend)

# Compute FFT for all waves
fft_combined_wave = fft(combined_wave)
fft_wave_with_trend = fft(wave_with_trend)
fft_detrended_wave = fft(detrended_wave)
fft_filtered_wave_trend = fft(filtered_wave_trend)

# Compute power spectra
power_spectrum_combined = np.abs(fft_combined_wave) ** 2
power_spectrum_wave_with_trend = np.abs(fft_wave_with_trend) ** 2
power_spectrum_detrended = np.abs(fft_detrended_wave) ** 2
power_spectrum_filtered_trend = np.abs(fft_filtered_wave_trend) ** 2

# Normalize power spectra
power_spectrum_combined_normalized = power_spectrum_combined / np.max(power_spectrum_combined)
power_spectrum_wave_with_trend_normalized = power_spectrum_wave_with_trend / np.max(power_spectrum_wave_with_trend)
power_spectrum_detrended_normalized = power_spectrum_detrended / np.max(power_spectrum_detrended)
power_spectrum_filtered_trend_normalized = power_spectrum_filtered_trend / np.max(power_spectrum_filtered_trend)

# Plot the normalized power spectra
plt.figure(figsize=(12, 12))

plt.subplot(4, 1, 1)
plt.plot(freqs, power_spectrum_combined_normalized)
plt.title('Normalized Power Spectrum of Combined Wave (5 Hz, 10 Hz, 15 Hz)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Normalized Power')
plt.xlim(0, 20)

plt.subplot(4, 1, 2)
plt.plot(freqs, power_spectrum_wave_with_trend_normalized)
plt.title('Normalized Power Spectrum of Wave with Linear Trend Added')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Normalized Power')
plt.xlim(0, 20)

plt.subplot(4, 1, 3)
plt.plot(freqs, power_spectrum_detrended_normalized)
plt.title('Normalized Power Spectrum of Detrended Wave (Linear Detrend)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Normalized Power')
plt.xlim(0, 20)

plt.subplot(4, 1, 4)
plt.plot(freqs, power_spectrum_filtered_trend_normalized)
plt.title('Normalized Power Spectrum of Filtered Wave (Butterworth High-Pass Filter)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Normalized Power')
plt.xlim(0, 20)

plt.tight_layout()
plt.show()
