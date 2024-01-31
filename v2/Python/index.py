from Database import Xemote
import threading
import time



# Get and print the system's UUID
system_uuid = obj.get_uuid()

if system_uuid:
    print("System UUID:", system_uuid)
else:
    print("Unable to retrieve system UUID.")

# obj.screenshot()
# obj.get()
del obj