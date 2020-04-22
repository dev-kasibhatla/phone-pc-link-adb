from subprocess import Popen, PIPE
import subprocess
import DataManager
import Commands as com
import Control as con

def ex(action):
    prefix="adb shell input touchscreen "
    command = prefix+action
    print(command)
    p = subprocess.Popen(command, shell=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    #print(stdout)
    #print(stderr)

def do(action):
    e(com.getTap(action))

def e(action):
    process.stdin.write(('input '+action+'\n').encode())
    process.stdin.flush()
    #print(repr(process.stdout.readline())) # Should print output


def closeShell():
    process.stdin.close()
    print('Waiting for adb shell to exit')
    process.wait()
    print('adb shell finished with return code %d' % process.returncode)

# process = Popen(['adb shell\n'],shell=True, stdin=PIPE, stdout=PIPE)

# com.init()

# while(1):
#     ip = input("Command: ")
#     if ip == 's':
#         do("shoot")
#     elif ip == 'j':
#         do("jump")
#     else:
#         break

# closeShell()


#work on control
con.init()