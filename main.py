import controls
import time
import engine_factory
from audio_device import AudioDevice

#engine = engine_factory.v_8_LS()
engine = engine_factory.inline_4_uneven_firing()

audio_device = AudioDevice()
stream = audio_device.play_stream(engine.gen_audio)

print('\nEngine is running...')

try:
    controls.capture_input(engine)  # blocks until user exits
except KeyboardInterrupt:
    pass

print('Exiting...')
stream.close()
audio_device.close()
