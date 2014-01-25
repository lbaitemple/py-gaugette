import gaugette.ssd1306
import time
import sys

RESET_PIN = "P9_15"
DC_PIN    = "P9_16"

print("init")
led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN, rows=64,cols=128)
print("begin")
led.begin()
print("clear")
led.clear_display()
led.display()

led.invert_display()
time.sleep(1)
led.normal_display()
time.sleep(1)

offset = 0 # flips between 0 and 32 for double buffering

while True:

    # write the current time to the display on every other cycle
    if offset == 0:
        text = time.strftime("%A")
	print("draw")
        led.draw_text2(0,0,text,2)
        text = time.strftime("%e %b %Y")
	print("draw")
        led.draw_text2(0,16,text,2)
        text = time.strftime("%X")
	print("draw")
        led.draw_text2(0,32+4,text,3)
	print("display")
        led.display()
        time.sleep(0.2)
    else:
        time.sleep(0.5)
        
    # vertically scroll to switch between buffers
    for i in range(0,32):
        offset = (offset + 1) % 64
	print("scroll")
        led.command(led.SET_START_LINE | offset)
        time.sleep(0.01)
