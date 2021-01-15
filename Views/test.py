import os
import signal
import subprocess

pid = 11556
res = os.kill(pid,signal.SIGKILL)
if not res:
    subprocess.call('exit()',shell=True)