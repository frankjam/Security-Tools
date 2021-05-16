import os
import subprocess
# execute the subprocess
data = subprocess.check_output(['netsh','wlan','show','profile']).decode('utf-8').split('\n')

y='All User Profile     :'
command ='netsh wlan show profile '
keys = ' key=clear'
for x in data:
    if(y in x):
       print(os.system( command + x.strip(y) + keys))