import time

print(time.time())
print(time.localtime())
print(time.gmtime(0))

# two working methods for calculating the local time
# 1 st method ... but we are not sure what represents the index,.. whether year or month
# so be careful using this method
time_here = time.localtime()
print("Year: ", time_here[0])
print("Month: ", time_here[1])
print("Day: ", time_here[2])
print("Hour: ", time_here[3])
print("Min: ", time_here[4])

# Second method
print("**" * 40)
local_time = time.localtime()
print("Year: ", local_time.tm_year)
print("Month: ", local_time.tm_mon)
print("Day: ", local_time.tm_mday)
print("Hour: ", local_time.tm_hour)
print("Minutes: ", local_time.tm_min)

# let's play a short time game
import time, random
from time import time as my_timer
print("**" * 40)

input("Press enter to start")
wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()

input("Press enter to stop")
end_time = my_timer()

print("You started at " + time.strftime("%X", time.localtime(start_time)))
print("You end at " + time.strftime("%X", time.localtime(end_time)))
print("Your reaction time was {} seconds".format(end_time - start_time))

# in the place of time imported, we can also import
from time import perf_counter as my_timer # accurate wait time but doesn't provide final accurate result
# or
from time import monotonic as my_timer # also works



