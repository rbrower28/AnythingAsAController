# Controller Emulation Scripts for Windows

Ever seen that video of the guy who plays COD with a recorder?
Or the guy who beats Doom with a guitar hero controller?
What about the girl that plays Elden Ring with the intensity of her brain waves?

Ever wonder how they do it?

## Controller Emulation Script

First, the script `controller_out.py` contains a python class that uses **vgamepad** to emulate an Xbox 360 gamepad. When `handle_input()` is called, it takes the list of inputs and activates them on the emulated controller.

## Input Script (Listener)

This is where the possibilities run wild.

Ever want to beat a dark souls boss by shouting commands?
How about by playing the piano? By doing sign language? On a dance dance revolution mat? The options are endless.

### **Current Scripts**

- `keyboard_in.py`
  - The most basic example. Uses the **keyboard** library to listen for key inputs. Rewrite the key map in the beginning to play any game with the keys on your keyboard.

- `ukulele_in.py`
  - This script uses **pyaudio** to listen through your default microphone, **numpy** to convert the raw audio, and **aubio** to isolate the pitch in hertz. Currently only configured for one octave of the major scale.

### **Input Item Backlog**

- MIDI keyboard
- Saying commands into microphone
- Sign language (webcam with OpenCV)
- Wind instrument (piggyback off ukulele, maybe create universal note control)
- DDR pad
- Electric guitar

## Test Script

Fortunately, the **xinput** library provides a test script for us to see how our controller emulator is being seen by our device. Run `_test_/xinput_api_test.py`, then in a separate terminal start your controller "in" script. Controller inputs will highlight as your program creates them.

*I did not write the xinput test script. Credit where credit is due*