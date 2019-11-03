import time
import bimpy
import functions

ctx = bimpy.Context()

ctx.init(250, 150, "Clock")

while(not ctx.should_close()):
    with ctx:
        t = clock.gettime()
        beats = clock.toswatch(t)
        bimpy.begin("Time")
        bimpy.set_window_font_scale(2)
        bimpy.text("@{:.2f}".format(beats))
        bimpy.end()

        b = clock.getdate()
        dates = clock.toWorld(b)
        bimpy.begin("Date")
        bimpy.set_window_font_scale(2)
        bimpy.text("{}".format(dates))
        bimpy.end()
        time.sleep(1/60)
