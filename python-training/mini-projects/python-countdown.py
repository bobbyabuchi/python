import time

time_seconds = 10
while time_seconds > 0:
    print(time_seconds)
    time.sleep(1)
    time_seconds -= 1
print("Time Up!")
