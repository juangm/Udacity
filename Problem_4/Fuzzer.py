# Watch the videos from Charlie Millers
# "Babysitting an Army of Monkeys"
# Part1 - youtube.com/watch?v=Xnwodi2CBws

# List of files to use as initial seed
file_list = ["Test1.pdf", "Test2.pdf", "Test3.pdf", "Test4.pdf"]

#List of applications to test
apps = ["/Program Files/Adobe/Reader 11.0/Reader/AcroRd32"]

fuzz_out = "result.pdf"

FuzzFactor = 100
num_test = 100

# END configuration

import math
import random
import string
import subprocess
import time

for i in range(num_test):
    file_choice = random.choice(file_list)
    app = apps
    
    buf = bytearray(open(file_choice, 'rb').read())
    
    # Start Charlie Miller code
    numwrites = random.randrange(math.ceil(float(len(buf)) / FuzzFactor))+1
    
    for j in range(numwrites):
        rbyte = random.randrange(256)
        rn = random.randrange(len(buf))
        buf[rn] = "%c"%(rbyte)
    # END code Charlie miller
    
    open(fuzz_out, 'wb').write(buf)
    
    process = subprocess.Popen([app, fuzz_out])
    
    time.sleep(1)
    crashed = process.poll()
    if not crashed:
        process.terminate()