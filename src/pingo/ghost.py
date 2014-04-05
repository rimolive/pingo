from pingo.board import Board
from pingo.board import DigitalPin, GroundPin, VddPin

class GhostBoard(Board):

    def __init__(self):

        pins = [
            GroundPin(self, 1),
            VddPin(self, 2, "xV"),
            DigitalPin(self, 13),
        ]

        self.add_pins(pins)

    def set_pin_mode(self, pin, mode):
        pass

    def set_pin_state(self, pin, state):
        pass