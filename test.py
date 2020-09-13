import subprocess
import sys
subprocess.call('pwd', shell=True)
subprocess.call('sh test.sh file.name', shell=True)
print(sys.argv[0])