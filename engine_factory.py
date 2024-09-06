import synth
import audio_tools
from engine import Engine
import random as rd


_fire_snd = synth.sine_wave_note(frequency=160, duration=1)
audio_tools.normalize_volume(_fire_snd)
audio_tools.exponential_volume_dropoff(_fire_snd, duration=0.06, base=5)

def inline_4_uneven_firing():
    whynot=4
    mini = 170
    maxi = 190
    return Engine(
        idle_rpm=800,
        limiter_rpm=7800,
        strokes=4,
        cylinders=whynot,
        timing=[rd.uniform(mini, maxi), rd.uniform(mini, maxi), rd.uniform(mini, maxi), rd.uniform(mini, maxi)],
        fire_snd=_fire_snd,
        between_fire_snd=synth.silence(1)
    )
