'''

(Current time) Listing 2.7, ShowCurrentTime.py, gives a program that displays the
current time in GMT. Revise the program so that it prompts the user to enter the
time zone in hours away from (offset to) GMT and displays the time in the speci-
fied time zone. Here is a sample run

Enter the time zone offset to GMT: -5
The current time is 4:50:34

'''
import time

currentTime = int(time.time())
current_seconds = currentTime % 60
minutes = currentTime // 60
current_minutes = minutes % 60
hours = minutes // 24
current_hour = hours % 24



print("Time is ",current_hour,":",current_minutes,":",current_seconds, "GMT" )