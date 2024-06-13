import time
import sys
rounds = 10
def animate():
    sys.stdout.write('\rloading |')
    time.sleep(0.2)
    sys.stdout.write('\rloading /')
    time.sleep(0.2)
    sys.stdout.write('\rloading -')
    time.sleep(0.2)
    sys.stdout.write('\rloading \\')
    time.sleep(0.2)
    sys.stdout.write('\rloading |')
    time.sleep(0.2)
    sys.stdout.write('\rloading /')
    time.sleep(0.2)
    sys.stdout.write('\rloading -')
    time.sleep(0.2)
    sys.stdout.write('\rloading \\')
    time.sleep(0.2)
done = False
def loading(done):
    while done == False:
        animate()
        done = True
        sys.stdout.write('\rDone!    \n')


