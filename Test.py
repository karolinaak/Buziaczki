import time
import rtmidi

mo = rtmidi.MidiOut()
for port_no in range(mo.get_port_count()):
		port_name = mo.get_port_name(port_no)
		print("MIDI out:", port_name)
		if port_name.find('Launchpad Mini')>-1:
			midi_port = mo.open_port(port_no)

def display_grid():
	midi_port.send_message([0x90, 2, 27])
	midi_port.send_message([0x90, 5, 27])
	midi_port.send_message([0x90, 18, 27])
	midi_port.send_message([0x90, 21, 27])
	midi_port.send_message([0x90, 32, 27])
	midi_port.send_message([0x90, 33, 27])
	midi_port.send_message([0x90, 34, 27])
	midi_port.send_message([0x90, 35, 27])
	midi_port.send_message([0x90, 36, 27])
	midi_port.send_message([0x90, 37, 27])
	midi_port.send_message([0x90, 38, 27])
	midi_port.send_message([0x90, 39, 27])
	midi_port.send_message([0x90, 50, 27])
	midi_port.send_message([0x90, 53, 27])
	midi_port.send_message([0x90, 66, 27])
	midi_port.send_message([0x90, 69, 27])
	midi_port.send_message([0x90, 80, 27])
	midi_port.send_message([0x90, 81, 27])
	midi_port.send_message([0x90, 82, 27])
	midi_port.send_message([0x90, 83, 27])
	midi_port.send_message([0x90, 84, 27])
	midi_port.send_message([0x90, 85, 27])
	midi_port.send_message([0x90, 86, 27])
	midi_port.send_message([0x90, 87, 27])
	midi_port.send_message([0x90, 98, 27])
	midi_port.send_message([0x90, 101, 27])
	midi_port.send_message([0x90, 114, 27])
	midi_port.send_message([0x90, 117, 27])
