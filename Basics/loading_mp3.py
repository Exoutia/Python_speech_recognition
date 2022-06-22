from pydub import AudioSegment

audio = AudioSegment.from_wav("output.wav")

#increae volume by 6db
audio += 6
audio *= 2
audio = audio.fade_in(200)
audio.export("Mps.mp3", format= "mp3")
audio2 = AudioSegment.from_mp3("Mps.mp3")
