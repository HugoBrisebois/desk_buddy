import time

from st7789v.interface import RaspberryPi
from st7789v import BufferedDisplay


with RaspberryPi() as rpi:

# init the display
display = BufferedDisplay(rpi, rotation=270)

# show black buffer (empty buffer)
display.update
time.sleep(0.5)

# draw a blue rectangle
display.draw.rectangle((0, 0, 320, 240), fill='blue')

# update only the top halfof the screen
display.update_partial(0, 0, 320, 120)