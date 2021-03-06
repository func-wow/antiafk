# @Date:   2020-06-17T19:51:28-04:00
# @Last modified time: 2020-08-27T10:34:20-04:00


import os
import time
import argparse
import random
import multiprocessing

import keyboard
from inputimeout import inputimeout, TimeoutOccurred
# import pyautogui


# Define range of random jump intervals
params = {'bg': (15, 200),
          'city': (90, 600),
          }

def enter_battle():
    """Automatically joins a battleground.

    """
    while True:
        time.sleep(30)
        enter_button = pyautogui.locateOnScreen('./images/enter-battle.png')
        if enter_button is not None:
            print('Joining BG')
            point = pyautogui.center(enter_button)
            pyautogui.click(*point)

def idle(loc):
    """Idles by pressing the space bar at random intervals.

    Args:
        loc (:obj:`str`): idling location ('bg' or 'city').
    """
    print('Starting in 5s')
    time.sleep(5)

    while True:
        keyboard.press_and_release('space')
        delay = random.randint(*params[loc])
        print(f'Next in {delay}s')
        time.sleep(delay)

def shutdown():
    """Powers down the computer after maximum idle time is reached.
    Useful when going to bed during that last AV game of the night.
    """
    timeout = 30
    prompt = f'Press any key within {timeout}s to cancel shutdown'

    try:
        answer = inputimeout(prompt=prompt, timeout=timeout)
    except TimeoutOccurred:
        answer = None

    if answer is not None:
        print('Shutdown cancelled.')
    else:
        print('Bye!')
        keyboard.press_and_release('enter, /, e, x, i, t, enter')
        os.system('shutdown /s /t 5')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Idle helper.')
    parser.add_argument('loc', default=['bg'], nargs='*', help='bg or city')
    parser.add_argument('-t', type=float, default=None, help='Idle duration')
    parser.add_argument('-s', action='store_true', help='Shutdown after')
    parser.add_argument('-j', action='store_true', help='Auto join BG')
    args = parser.parse_args()

    if args.t is not None:
        args.t = 3600*args.t
        print(f'Max idle time {args.t:.0f}s')

    if args.j:
        j = multiprocessing.Process(target=enter_battle)
        j.start()

    p = multiprocessing.Process(target=idle, args=(args.loc[0],))
    p.start()
    p.join(args.t)

    if p.is_alive():
        print('\n    Process terminated.\n')
        p.terminate()
        if args.j:
            j.terminate()

    if args.s:
        shutdown()
