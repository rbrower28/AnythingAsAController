from controller_out import Controller
import pyaudio
import numpy as np
import aubio
import keyboard

# initialise pyaudio
p = pyaudio.PyAudio()

# open stream
buffer_size = 1024
pyaudio_format = pyaudio.paFloat32
n_channels = 1
samplerate = 44100
stream = p.open(format=pyaudio_format,
                channels=n_channels,
                rate=samplerate,
                input=True,
                frames_per_buffer=buffer_size)


# setup pitch
tolerance = 0.8
win_s = 4096 # fft size
hop_s = buffer_size # hop size
pitch_o = aubio.pitch("default", win_s, hop_s, samplerate)
pitch_o.set_unit("Hz")
pitch_o.set_tolerance(tolerance)


uke_freq = {
    "C": 260,
    "D": 293,
    "E": 330,
    "F": 350,
    "G": 392,
    "A": 440,
    "B": 494,
    "CC": 525,
}

# calculate note based on pitch
def calculate_note(pitch, margin, freq):

    if (freq["C"] - margin < pitch < freq["C"] + margin):
        return "C"
    elif (freq["D"] - margin < pitch < freq["D"] + margin):
        return "D"
    elif (freq["E"] - margin < pitch < freq["E"] + margin):
        return "E"
    elif (freq["F"] - margin < pitch < freq["F"] + margin):
        return "F"
    elif (freq["G"] - margin < pitch < freq["G"] + margin):
        return "G"
    elif (freq["A"] - margin < pitch < freq["A"] + margin):
        return "A"
    elif (freq["B"] - margin < pitch < freq["B"] + margin):
        return "B"
    elif (freq["CC"] - margin < pitch < freq["CC"] + margin):
        return "CC"
    else:
        return ""

# only enough notes for really basic games...
control_map = {
    "C": "LLEFT",
    "D": "LRIGHT",
    "E": "A",
    "F": "X",
    "G": "B",
    "A": "R2",
    "B": "LDOWN",
    "CC": "LUP",
}


MARGIN = 10

c = Controller()
active_note = []

print("*** starting recording")
while True:
    audiobuffer = stream.read(buffer_size)
    signal = np.frombuffer(audiobuffer, dtype=np.float32)

    pitch = pitch_o(signal)[0]

    note = calculate_note(pitch, MARGIN, uke_freq)
    if note:
        active_note.append(control_map[note])
        print("Estimated Note:", note)
    
    c.handle_input(active_note)

    active_note.clear()

    if keyboard.is_pressed("esc"):
        break


print("*** done recording")
stream.stop_stream()
stream.close()
p.terminate()
