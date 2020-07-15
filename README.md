# antiafk
Python script to avoid getting booted.

## Installation
1. Download and install [Python](https://www.python.org/ftp/python/3.8.4/python-3.8.4.exe)
2. Download this repository to your computer
3. Open the Windows PowerShell or Command Prompt
4. Enter `pip install inputimeout`
5. Enter `pip install keyboard`

## Usage
1. Navigate to the previously downloaded antiafk folder
2. Shift+RightClick anywhere in that folder
3. Click Open PowerShell window here
4. Enter `python antiafk.py`

## Options
### Jump frequency
Specify the `bg` or `city` option if you are afking in a city or BG. When not specified, the `bg` option is used by default. Using the `city` option in a BG will probably hit you with deserter.  
For example, 
```
python antiafk.py city
``` 
will idle with a slow jump frequency (ideal for idling during queue).

- *'bg' jumps happen every 15 to 200 seconds.*
- *'city' jumps happen every 90 to 600 seconds.*

### Program timeout
Use the `-t` option to specify a time limit on running the script. 
For example, 
```
python antiafk.py city -t 2.5
``` 
will idle for 2.5 hours using 'city' intervals then turn off the program.

### Automated computer shutdown
Use the `-s` option to automatically shutdown the computer after the time period specified by `-t`.
For example, 
```
python antiafk.py bg -t 1 -s
```
will idle for 1 hour using 'bg' intervals then turn off the program and shutdown the computer.  
There is a 30 seconds grace period at the end of the time limit where you can hit any key to cancel the shutdown. Don't use the `-s` option without specifying the `-t` limit.
