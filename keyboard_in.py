from controller_out import Controller
import keyboard

c = Controller()
inputs = []

input_map = {
    "w": "LUP",
    "s": "LDOWN",
    "a": "LLEFT",
    "d": "LRIGHT",

    "up": "RUP",
    "down": "RDOWN",
    "left": "RLEFT",
    "right": "RRIGHT",

    "f": "DUP",
    "v": "DDOWN",
    "c": "DLEFT",
    "b": "DRIGHT",

    "k": "A",
    "l": "B",
    "i": "X",
    "o": "Y",

    "j": "L1",
    ";": "R1",
    "u": "L2",
    "p": "R2",

    "z": "L3",
    "x": "R3",

    "e": "START",
    "q": "SELECT"
}

while not keyboard.is_pressed("esc"):

    for item in input_map.keys():
        if keyboard.is_pressed(item):
            inputs.append(input_map[item])

    c.handle_input(inputs)
    inputs.clear()

print(">>>>> Program finished. >>>>>")