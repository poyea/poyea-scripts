import matplotlib.pyplot as plt
import numpy as np
import pyaudio

volume = 0.05
duration_seconds = 3
fs = 44100  # sampling rate, Hz, must be integer
f = 440.0  # sine frequency, Hz, may be float


if __name__ == "__main__":
    assert 0.0 <= volume <= 1.0
    p = pyaudio.PyAudio()

    T = 1 / (f / fs)
    shah = np.arange(fs * duration_seconds)
    samples = (np.sin(2 * np.pi / T * shah)).astype(np.float32)

    plt.xlim([0, T])
    plt.plot(samples)
    plt.show()

    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
    stream.write(volume * samples)
    stream.stop_stream()
    stream.close()

    p.terminate()
