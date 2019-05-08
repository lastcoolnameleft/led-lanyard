import random
import time
from effects.ws2811 import Controller

queue_file = '/tmp/messages.queue'
max_brightness = 150
num_pixels = 144


def get_command(queue_file):
    command = None
    with open(queue_file, 'r') as fin:
        data = fin.read().splitlines(True)
        if data:
            command = data[0].rstrip()
    with open(queue_file, 'w') as fout:
        fout.writelines(data[1:])
    return command

command = None

while True:
    random.seed()

    command = get_command(queue_file)

    if command == 'black':
        Controller.fill_black()
    elif command == 'red':
        Controller.fill_red()
    elif command == 'blue':
        Controller.fill_blue()
    elif command == 'green':
        Controller.fill_green()
    elif command == 'fill-random':
        Controller.fill_random()
    elif command == 'msft':
        msftColorGroup = ((max_brightness, 0, 0), (0, max_brightness, 0), (0, 0, max_brightness), (max_brightness, max_brightness, 0)) 
        Controller.colorAllColorGroup(msftColorGroup) 
    elif command == 'fadeinout':
        Controller.FadeInOut(0, 255, 0, 0)
    elif command == 'chase':
        chaseObj = ((0,5,0), (0,10,0), (0,20,0), (0,30,0), (0,40,0), (0,50,0), (0,60,0), (0,70,0)) 
        Controller.colorAllColorGroup(chaseObj)
        Controller.RotateExisting(.1, 100)
    elif command == 'chase2':  # Not as impressive 
        cbreObj = ((0,5,0), (0,10,0), (0,20,0), (0,30,0), (0,40,0), (0,50,0), (0,60,0), (0,70,0)) 
        Controller.theaterChaseCustom(cbreObj, 5, 4, 0.2)
    elif command == 'follow':
        Controller.candycane_custom((200,200,200), (0,200,0), 255, 0.1, 10)
    elif command == 'fire':
        Controller.FireCustomMirror(0, 10, 20, 0, int(num_pixels/15), 1, 0.01, 900) # red fire
        #FireCustomMirror(0, 10, 20, 0, int(num_pixels/15), 2, 0.01, 900) # green fire
    elif command == 'fire-custom':  # Doesn't work
        Controller.FireCustom(0, 5, 70, 0, int(num_pixels/10), 1, 0.005, 900) # red fire
        #FireCustomMirror(0, 10, 20, 0, int(num_pixels/15), 2, 0.01, 900) # green fire
    elif command == 'levels-colors':
        cw = (255,255,255)
        cr = (255,0,0)
        cg = (0,255,0)
        cb = (0,0,255)
        cy = (255,255,0)
        #levels = (43, 73, 103, 135, 160, 188, 213, 236, 255, 272, 286, 295, 300)
        #levels = (58, 108, 149, 187, 224, 264, 292, 300)
        #levels = (110, 200, 270, 300)
        levels = (10,20,30,40,50,60,70,80,90,100,110,120,130,140,144)
        colorobj = ( cw, cg, cg, cw, cg, cg, cw, cw, cw) 
        Controller.LevelsColorsCustom(colorobj, levels, .5)
    elif command == 'sparkle':
        cbreObj = ((0,5,0), (0,5,0), (0,10,0), (0,10,0), (0,20,0), (0,20,0), (0,10,0), (0,10,0)) 
        Controller.colorAllColorGroup(cbreObj)
        Controller.SnowSparkleExisting(100, .1, .1)
    elif command == 'follow2':
        Controller.colorAll2Color((200,200,200), (0, 200, 0)) 
        Controller.RunningLightsPreExisting(.2, 100)
    elif command == 'heartbeat': # Couldn't get to work
        Controller.HeartBeatExisiting(3, .005, .003, 0.001, 6, .002, .003, 0.05, 1)
    else:
        #print('skipping')
        time.sleep(1)