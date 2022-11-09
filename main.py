import numpy as np
import pprint
import matplotlib.pyplot as plt
sample_rate = 44100

def get_wave(freq, duration =0.5):
    amplitude =4096
    t = np.linspace(0, duration, int(sample_rate *duration))
    wave = amplitude *np.sin(2 * np.pi * freq *t)
    
    return wave

def get_piano_notes():
    octave =['C','c','D','d','E','F','f','G','g','A','a','B']
    base_freq=261.63
    
    note_freqs ={octave[i]:base_freq *pow(2, (i/12)) for i in range(len(octave))}
    note_freqs ['']=0.0
    
    return  note_freqs

if __name__ == '__main__':
    pprint.pprint(get_piano_notes())