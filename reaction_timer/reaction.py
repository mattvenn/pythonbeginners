#import the libraries
import time
import random

#pick a random number and store in sleep_time
sleep_time = random.randint(3,10)

#sleep for sleep_time seconds
time.sleep(sleep_time)

#print "GO!"
print("GO!")

#store the current time in start_time
start_time = time.time()

#wait for the subject to press the 'enter key'
raw_input()

#work out how long they took by subtracting the start_time now from the time now
reaction_time = time.time() - start_time

#print out how long they took
print(reaction_time)


