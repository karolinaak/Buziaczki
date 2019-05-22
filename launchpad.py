# https://github.com/maciejjankowski/launchpad-mini-starter
# https://global.novationmusic.com/support/downloads/launchpad-programmers-reference-guide

import rtmidi

COLOR_X = <something>
COLOR_O = <something>

def connect_to_device(which_port='Launchpad Mini'):
  mo = rtmidi.MidiOut()
    for port_no in range(mo.get_port_count()):
            port_name = mo.get_port_name(port_no)
            print("MIDI out:", port_name)
            if port_name.find(which_port) > -1: 
                # or 'Launchpad Pro Standalone Port'
                midi_port = mo.open_port(port_no)
                return midi_port

# change x, y -> launchpad_position
def translate_board_position():
  pass

def draw_launchpad_board():
  pass

def get_pushed_button_coords():
  print("not needed now")
  pass

def turn_on_pixel():
  pass