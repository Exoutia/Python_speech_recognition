import wave 
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("sample.wav", "rb")

sample_freq = obj.getframerate()
n_sample = obj.getnframes()
sample_wave = obj.readframes(-1)

obj.close()

t_audio = n_sample/sample_freq
print(t_audio)

signal_arr = np.frombuffer(sample_wave, dtype=np.int16)

time = np.linspace(0, t_audio, num = n_sample)




