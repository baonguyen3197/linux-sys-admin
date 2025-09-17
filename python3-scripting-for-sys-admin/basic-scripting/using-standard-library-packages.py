# timer

import time

start_time = time.localtime()
print(f"Timer starts at {time.strftime('%X', start_time)}")

# Wait for user to stop timer
input("Press 'Enter' to stop the timer... ")

stop_time = time.localtime()
diff = time.mktime(stop_time) - time.mktime(start_time)

print(f"Timer stopped at {time.strftime('%X', stop_time)}")
print(f"'Total time: {diff:.2f} seconds'")

# /////////////////////////////////////////////////////////////// #
from time import localtime, strftime, mktime

start_time = localtime()
print(f"Timer starts at {strftime('%X', start_time)}")

# Wait for user to stop timer
input("Press 'Enter' to stop the timer... ")

stop_time = localtime()
diff = mktime(stop_time) - mktime(start_time)

print(f"Timer stopped at {strftime('%X', stop_time)}")
print(f"'Total time: {diff:.2f} seconds'")
