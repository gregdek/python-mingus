#!/usr/bin/python

from mingus.midi import midi_file_out
from mingus.containers import NoteContainer

nc = NoteContainer(["A", "C", "E"])
midi_file_out.write_NoteContainer("test.mid", nc)
