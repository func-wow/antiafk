# @Date:   2020-06-17T19:51:28-04:00
# @Last modified time: 2020-07-08T06:53:05-04:00


import os
import time
import argparse
import random
import multiprocessing

import keyboard
from inputimeout import inputimeout, TimeoutOccurred


params = {'bg': (15, 200),
          'city': (90, 600),
          }

def idle(loc):
    print('Starting in 5s')
    time.sleep(5)

    while True:
        keyboard.press_and_release('space')
        delay = random.randint(*params[loc[0]])
        print(f'Next in {delay}s')
        time.sleep(delay)


def shutdown():
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
    parser.add_argument('loc', type=str, default='bg', nargs='*', help='bg or city')
    parser.add_argument('-t', type=float, default=None, help='Idle duration')
    parser.add_argument('-s', action='store_true', help='Shutdown after')
    args = parser.parse_args()

    if args.t is not None:
        args.t = 3600*args.t
        print(f'Max idle time {args.t:.0f}s')

    p = multiprocessing.Process(target=idle, args=(args.loc,))
    p.start()
    p.join(args.t)

    if p.is_alive():
        print('\n    Process terminated.\n')
        p.terminate()
        p.join()

    if args.s:
        shutdown()
