import time
import bimpy
import clock

ctx = bimpy.Context()

ctx.init(250, 150, "Clock")

t = clock.gettime()
beats = clock.toswatch(t)


while(not ctx.should_close()):
    with ctx:
        time.sleep(1/60)
        t = clock.gettime()
        beats = clock.toswatch(t)
        bimpy.begin("Local Swatch Time")
        bimpy.set_window_font_scale(2)
        bimpy.text("@{:.2f}".format(beats))
        bimpy.end()
