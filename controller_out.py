import vgamepad as vg

class Controller:
    """ Emulates an Xbox 360 controller.
        Recognized inputs:
        A B X Y
        LUP LDOWN LLEFT LRIGHT
        RUP RDOWN RLEFT RRIGHT
        DUP DDOWN DLEFT DRIGHT
        L1 L2 L3
        R1 R2 R3
        START SELECT
    """
    
    # controller obj
    gamepad = vg.VX360Gamepad()

    # current key memory
    keys_down = set()

    # left thumb stick
    xL = 0.0
    yL = 0.0

    # right thumb stick
    xR = 0.0
    yR = 0.0

    # triggers
    L2 = 0.0
    R2 = 0.0

    button_map = {
        "A": vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
        "B": vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
        "X": vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
        "Y": vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,

        "DUP": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
        "DDOWN": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
        "DLEFT": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
        "DRIGHT": vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,

        "START": vg.XUSB_BUTTON.XUSB_GAMEPAD_START,
        "SELECT": vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK,

        "L1": vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
        "R1": vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,

        "L3": vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB,
        "R3": vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB
    }

    stick_map = {
        "LUP":    (0.0, 0.8),
        "LDOWN":  (0.0, -0.8),
        "LLEFT":  (-0.8, 0.0),
        "LRIGHT": (0.8, 0.0),

        "RUP":    (0.0, 0.8),
        "RDOWN":  (0.0, -0.8),
        "RLEFT":  (-0.8, 0.0),
        "RRIGHT": (0.8, 0.0),
    }

    def handle_input(self, controls):

        for item in self.button_map.keys():
            if item in controls:
                if item not in self.keys_down:
                    self.gamepad.press_button(self.button_map[item])
                    self.keys_down.add(item)
            else:
                if item in self.keys_down:
                    self.gamepad.release_button(self.button_map[item])
                    self.keys_down.remove(item)

        for item in self.stick_map.keys():
            if item in controls:
                if item[0] == "L":
                    if item not in self.keys_down:
                        self.xL += self.stick_map[item][0]
                        self.yL += self.stick_map[item][1]
                        self.keys_down.add(item)
                elif item[0] == "R":
                    if item not in self.keys_down:
                        self.xR += self.stick_map[item][0]
                        self.yR += self.stick_map[item][1]
                        self.keys_down.add(item)
            else:
                if item[0] == "L":
                    if item in self.keys_down:
                        self.xL -= self.stick_map[item][0]
                        self.yL -= self.stick_map[item][1]
                        self.keys_down.remove(item)
                elif item[0] == "R":
                    if item in self.keys_down:
                        self.xR -= self.stick_map[item][0]
                        self.yR -= self.stick_map[item][1]
                        self.keys_down.remove(item)

        if "L2" in controls:
            if "L2" not in self.keys_down:
                self.L2 = 1.0
                self.keys_down.add("L2")
        else:
            if "L2" in self.keys_down:
                self.L2 = 0.0
                self.keys_down.remove("L2")

        if "R2" in controls:
            if "R2" not in self.keys_down:
                self.R2 = 1.0
                self.keys_down.add("R2")
        else:
            if "R2" in self.keys_down:
                self.R2 = 0.0
                self.keys_down.remove("R2")

        # apply changes to controller
        self.gamepad.left_joystick_float(x_value_float=self.xL, y_value_float=self.yL)
        self.gamepad.right_joystick_float(x_value_float=self.xR, y_value_float=self.yR)
        self.gamepad.left_trigger_float(value_float=self.L2)
        self.gamepad.right_trigger_float(value_float=self.R2)

        self.gamepad.update()