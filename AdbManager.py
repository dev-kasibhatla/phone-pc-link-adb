from subprocess import Popen, PIPE
import Commands as com

def e(action):
    global process
    print(action)
    process.stdin.write(('input '+action+'\n').encode())
    process.stdin.flush()
    return True
    #print(repr(process.stdout.readline())) # Should print output

def dot(action):
    e(com.getTap2(action))

def dos(action):
    e(com.getSwipe2(action))


def closeShell():
    global process
    process.stdin.close()
    print('Waiting for adb shell to exit')
    process.wait()
    print('adb shell finished with return code %d' % process.returncode)

process = Popen(['adb shell\n'],shell=True, stdin=PIPE, stdout=PIPE)
print("Process initialized")
