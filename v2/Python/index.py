from Database import Xemote
import threading
import time

# Main Driver
obj = Xemote()

# # Create a thread for checking and updating commands
# commands_thread = threading.Thread(target=obj.assign_server_command)
# commands_thread.daemon = True  # Set as a daemon thread to exit when the main program exits
# commands_thread.start()

# # Your main program code here

# # Example: Run a loop to print some messages
# while True:
#     print("Main program is running...")
#     time.sleep(1)

# Get and print the system's UUID
system_uuid = obj.get_uuid()

if system_uuid:
    print("System UUID:", system_uuid)
else:
    print("Unable to retrieve system UUID.")

# obj.screenshot()
# obj.get()
del obj