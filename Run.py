import os, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
print('\033[1;32m [•] Join Facebook Group')
os.system('xdg-open https://facebook.com/groups/240526195427860/')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from Dump import HAMI
    HAMI()
elif bit == '32bit':
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
