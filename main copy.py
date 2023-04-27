from Xlib import X, display
from Xlib.ext import xtest

# получаем дисплей
disp = display.Display()

# эмулируем нажатие левой кнопки мыши
xtest.fake_input(disp, X.ButtonPress, 1)
disp.sync()

# эмулируем отпускание левой кнопки мыши
xtest.fake_input(disp, X.ButtonRelease, 1)
disp.sync()