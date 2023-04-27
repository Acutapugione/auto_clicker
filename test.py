from pynput.mouse import Button, Controller

mouse = Controller()
#450, 356
while 1:
    print ("Current position: " + str(mouse.position))