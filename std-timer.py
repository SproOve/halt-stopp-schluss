import datetime as dt
import os, subprocess, json

json_path = os.path.join(os.getcwd()
, 'config.json')

with open(json_path, 'r') as f:
    config_dict = json.load(f)

#path
doneHour = config_dict.__getitem__('doneHour')
doneMinute = config_dict.__getitem__('doneMinute')

a = dt.datetime.now()
b = dt.datetime.now()

b = b.replace(hour=doneHour).replace(minute=doneMinute)

c = (b-a).total_seconds()


def shutdown_computer():
    if os.name == 'nt':
        cstr = str(c).replace('.0', '')
        cmd = 'shutdown /s /t ' + cstr
        # For Windows operating system
        os.system(cmd)
    elif os.name == 'posix':
        cstr = str(round(c/60)).replace('.0', '')
        # For Unix/Linux/Mac operating systems
        os.system('sudo shutdown now')
    else:
        print('Unsupported operating system.')


if c <= 0:
    c = 60.0
    
shutdown_computer()
    
    
    
    