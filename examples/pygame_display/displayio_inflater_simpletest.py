import os
from foamyguy_displayio_inflater.absolute_layout import AbsoluteLayout
from blinka_displayio_pygamedisplay import PyGameDisplay

os.chdir("..")
display = PyGameDisplay(width=800, height=600)

f = open("layouts/simpletest.json", "r")
layout_str = f.read()
f.close()
main_layout = AbsoluteLayout(display, layout_str)

display.show(main_layout.view)

#main_layout.sub_view_by_index(0).label.text = "Changed Text\nBy Index"
main_layout.sub_view_by_id("main_lbl").label.text = "Changed\nText By Id"

while True:
    if display.check_quit():
        break
