from launchpad import *
import time
import rtmidi

def change_x_y_(positions):
    board_positions = {
        1: [0,0],
        2: [0,1],
        3: [0,2],
        4: [1,0],
        5: [1,1],
        6: [1,2],
        7: [2,0],
        8: [2,1],
        9: [2,2],
    }   
    return board_positions.get(int(positions), "nothing")

def connect_to_device():
    mo = rtmidi.MidiOut()
    for port_no in range(mo.get_port_count()):
            port_name = mo.get_port_name(port_no)
            print("MIDI out:", port_name)
            if port_name.find('Launchpad Mini') > -1: 
                # or 'Launchpad Pro Standalone Port'
                midi_port = mo.open_port(port_no)
    while True:
        x = input("X or O: <enter>")
        if x == "X" or x == "x":
            midi_port.send_message([0x90,0,COLOR_X])
            midi_port.send_message([0x90,1,COLOR_X])
            midi_port.send_message([0x90,16,COLOR_X])
            midi_port.send_message([0x90,17,COLOR_X])
        if x == "O" or x == "o":
            midi_port.send_message([0x90,6,COLOR_O])
            midi_port.send_message([0x90,7,COLOR_O])
            midi_port.send_message([0x90,22,COLOR_O])
            midi_port.send_message([0x90,23,COLOR_O])

def display_launchpad_pixel():
    midi_port.send_message([0x90,6,28])
    midi_port.send_message([0x90,7,28])
    midi_port.send_message([0x90,22,28])
    midi_port.send_message([0x90,23,28])
        #midi_port.send_message(msg, button, color) # 7 and 28 are position and color, taken from the docs

display_launchpad_pixel 
midi_port = connect_to_device()
display_launchpad_pixel()
#display_X(midi_port)


"""
midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

if available_ports:
    midiout.open_port(0)
else:
    midiout.open_virtual_port("My virtual output")

note_on = [16, 15, 112] # channel 1, middle C, velocity 112
note_off = [0x80, 60, 0]
midiout.send_message(note_on)
time.sleep(0.5)
#midiout.send_message(note_off)

del midiout
"""
