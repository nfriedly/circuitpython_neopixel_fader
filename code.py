import board
import neopixel
import time
import colors

rgb = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.5, auto_write=True)

# rainbow
colorGenerator = colors.Fader(colors.RAINBOW, duration=3)

# red strobe
#colorGenerator = colors.Strober(color=colors.RED, duration=1)

# green breathing
#colorGenerator = colors.Fader((colors.GREEN, colors.BLACK), duration=6)

while True:
    if colorGenerator.update():
        rgb.fill(colorGenerator.color)
    time.sleep(0.01)