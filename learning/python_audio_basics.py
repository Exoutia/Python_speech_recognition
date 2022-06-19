# Audio File Formats 
# .mp3 // Compressed format
# .flac // Can be converted into original 
# .wav // original file with every property of audio

import wave

# Audio Signal Parameters
# - Number of channels -> 1 is mono - 2 is stereo
# - sample width
# - framerate/ sample_rate: 44,000 Hz (standard cd sample)
# - numbers of frames
# - Values of a frame


obj = wave.open("sample_1mb.wav", "rb")

print("Number of channels: ", obj.getnchannels())
print("sample width: ", obj.getsampwidth())
print("frame rate: ", obj.getframerate())
print("numbers of frames: ", obj.getnframes())
print("Parameters: ", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print(t_audio)
frames = obj.readframes(-1)

print(type(frames), type(frames[0]))
print(len(frames)/2)

obj.close()

obj_new = wave.open("sample_1mb_new.wav", "wb")

obj_new.setnchannels(1)
obj_new.setsampwidth(1)
obj_new.setframerate(16000.0)

obj_new.writeframes(frames)

obj_new.close()