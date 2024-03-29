# Class: Database
import mysql.connector
import json

# Class: Arsenal
import subprocess, cv2, pyautogui, pynput, ctypes
from datetime import datetime

# Class: Xemote
import time, uuid, threading

# Driver File
import pyuac

# License File
from os.path import exists as file_exists

'''====================================================================================================
# Title: Database (Class)
# ~ Description: Store Database Operations For Xemote
@methods:
    - put
    - get
    - __connect
    - __disconnect
    - __del__
@dependencies:
    - mysql.connector
    - json
@usage:
    obj = Database()
    obj.put()
    obj.get()
@notes:
    - This class is a collection of database operations for Xemote.
    - It uses the mysql.connector module for database operations.
    - It uses the json module for JSON operations.
    - It uses the put and get methods to update and retrieve data from the database.
    - It uses the __connect and __disconnect methods to connect and disconnect from the database.
    - It uses the __del__ method to perform cleanup.
@status: Completed
@version: 1.0
@date: 2021-09-30
@developer: Sami Rahman (srs404)
====================================================================================================
'''
class Database:
    # Constructor
    def __init__(self):
        # Database Connection Credentials Dictionary
        self.__db = {
            'server': 'localhost',
            'username': 'root',
            'password': '',
            'database': 'xemote'
        }
        # User Command Controller Dictionary
        self.user = {
            'userID': '123456', # User ID
            'active': False, # Subscription Status
            'command': {}, # JSON Data For Command
            'Ongoing': { # Ongoing Command Status
                'shutdown': False, # 0: No Command, 1: Shutdown, 2: Reboot, 3: Logoff
                'webcam': False,
                'screenshot': False,
                'blackout': False,
                'show_off': False,
                'shutdown_mayham': False,
                'upload_files': False
            },
            'db': {}, # Database Connection
        }
        self.__connect()

    '''
    Title: Python MySQL Connect
    ~ Description: Connect to MySQL database using a connection string
    '''
    def __connect(self):
        try:
            self.user['db']['connection'] = mysql.connector.connect(
                host=self.__db['server'],
                user=self.__db['username'],
                password=self.__db['password'],
                database=self.__db['database']
            )
            self.user['db']['cursor'] = self.user['db']['connection'].cursor()
        except Exception:
            print("Check Connection To Internet Or Server!")

    def __disconnect(self):
        self.user['db']['cursor'].close()
        self.user['db']['connection'].close()

    '''
    Title: Python MySQL Update Data
    ~ Description: Update MySQL database using a parameterized query
    '''
    def put(self):
        try:
            if not self.user['db']['connection'].is_connected():
                self.__connect()

            # Convert JSON data to a string
            json_data = json.dumps(self.user['command'])

            # Use a parameterized query to safely update the database
            sql = "UPDATE command_center SET command = %s WHERE user_id = %s"
            values = (json_data, 123456)  # Replace 123456 with your actual user_id

            self.user['db']['cursor'].execute(sql, values)
            self.user['db']['connection'].commit()

            self.__disconnect()

            return True
        except Exception as e:
            print("Error:", str(e))
            return False
    
    '''
    Title: Python MySQL Get Data
    ~ Description: Retrieve data from MySQL database using a parameterized query
    @return: True if successful, False otherwise
    '''

    def get(self, option="command"):
        try:
            if not self.user['db']['connection'].is_connected():
                self.__connect()

            # Use a parameterized query to safely retrieve data from the database
            if option == "uuid":
                sql = "SELECT uuid FROM command_center WHERE user_id = %s"
            else:
                sql = "SELECT command FROM command_center WHERE user_id = %s"
            values = (123456,)

            self.user['db']['cursor'].execute(sql, values)
            result = self.user['db']['cursor'].fetchone()

            self.__disconnect()

            # Check if any result was fetched
            if result and option == "command":
                self.user['command'] = json.loads(result[0])
            elif result and option == "uuid":
                return result[0]
            else:
                print("No data found")
                return None

        except Exception as e:
            print("Error:", str(e))
            return None

    # Destructor
    def __del__(self):
        self.__disconnect()

'''====================================================================================================
# Title: Arsenal (Class)
# ~ Description: Store Main Functions For Xemote
@methods:
    - webcam
    - blackout
    - screenshot
    - device_shutdown_state
    - __del__
@dependencies:
    - Database
    - subprocess
    - cv2
    - pyautogui
    - pynput
    - ctypes
@usage:
    obj = Arsenal()
    obj.webcam()
    obj.screenshot()
    obj.device_shutdown_state(1)
@notes:
    - This class is a collection of main functions for Xemote.
    - It inherits from the Database class.
    - It uses the subprocess module for system commands.
    - It uses the cv2 module for webcam operations.
    - It uses the pyautogui module for screenshot operations.
@status: Ongoing
@version: 1.0
@date: 2021-09-30
@developer: Sami Rahman (srs404)
@license: MIT (https://opensource.org/licenses/MIT)
@contact:
    - Email: mail@srs404.com
    - Website: https://srs404.com
    - GitHub: https://github.com/srs404
====================================================================================================
'''
class Arsenal(Database):
    def __init__(self):
        super().__init__()
        # Initialize the keyboard and mouse listeners with suppress=True to block input
        self.keyboard_listener = pynput.keyboard.Listener(suppress=True)
        self.mouse_listener = pynput.mouse.Listener(suppress=True)

    '''
    Title: Webcam
    ~ Description: Capture image from webcam
    Status: Completed
    '''
    def webcam(self):
        # Generate Timestamp
        def image_timestamp():
            current_datetime = datetime.now()
            return current_datetime.strftime("%d.%m.%Y-%H.%M.%S")
            
        filename = str(image_timestamp()) + ".jpg"

        # Create a VideoCapture object to access your webcam
        cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera (usually the built-in webcam)

        # Check if the camera is opened successfully
        if not cap.isOpened():      
            print("Error: Could not open camera.")
            exit()

        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            cap.release()
            cv2.destroyAllWindows()
            return
        
        # Save the captured frame to a file
        cv2.imwrite(filename, frame)

        # Release the VideoCapture and close the OpenCV window
        cap.release()
        cv2.destroyAllWindows()

    '''
    Title: Blackout
    ~ Description: Block or unblock keyboard keys
    Status: Completed
    '''
    def blackout(self, state):
        if state == "block":
            # Command to disable the Task Manager
            subprocess.run('REG add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f', shell=True)

            # Brightness: 0
            subprocess.run(["powershell", "(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,0)"])

            # Start the mouse listener to block mouse input
            self.mouse_listener.start()
            self.keyboard_listener.start()
        elif state == "unblock":
            # Command to enable the Task Manager
            subprocess.run('REG add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 0 /f', shell=True)

            # Brightness: 100
            subprocess.run(["powershell", "(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,100)"])

            # Stop the mouse listener to unblock mouse input
            self.mouse_listener.stop()
            self.keyboard_listener.stop()
            # Initialize the keyboard and mouse listeners with suppress=True to block input
            self.keyboard_listener = pynput.keyboard.Listener(suppress=True)
            self.mouse_listener = pynput.mouse.Listener(suppress=True)
        else:
            print("Invalid command")

    '''
    Title: Screenshot
    ~ Description: Capture screenshot of the screen
    Status: Completed
    '''
    def screenshot(self, filename="screenshot.jpg"):
        pyautogui.screenshot(filename)

    '''
    Title: Python MySQL Update Data
    ~ Description: Update MySQL database using a parameterized query
    '''
    def device_shutdown_state(self, state):
        if state in [1, 2, 3]:
            self.user['command']['shutdown'] = 0
            super().put()
            self.__del__()
        if state == 1:
            subprocess.call(["shutdown", "/s /f /t 0"])
        elif state == 2:
            subprocess.call(["shutdown", "/r /f /t 0"])
        elif state == 3:
            subprocess.call(["shutdown", "/l /f /t 0"])
        else:
            print("Invalid command")
        
        exit()

    def __del__(self):
        super().__del__()  # Call the parent class's __del__ method for cleanup

''' ====================================================================================================
# Title: Xemote (Class)
# ~ Description: Main Class For Xemote
@methods: 
    - get_system_uuid
    - get_uuid
    - __assign_server_command
    - execute
    - validate
    - __del__
@dependencies:
    - Database
    - Arsenal
    - time
    - platform
    - uuid
    - threading
@usage:
    obj = Xemote()
    obj.execute()
@notes:
    - This class is the main driver for Xemote.
    - It inherits from the Arsenal class.
    - It uses threading to run a separate thread for checking and updating commands.
    - It uses the platform and uuid modules to get the system's UUID.
    - It uses the time module for sleep.
    - It uses the threading module for creating a separate thread.
    - It uses the Database and Arsenal classes for database and system operations.
==================================================================================================== 
'''
class Xemote(Arsenal):
    def __init__(self):
        super().__init__()

    def get_uuid(self):
        try:
            # Run the shell command and capture the output
            output = subprocess.check_output(["wmic", "csproduct", "get", "uuid"], universal_newlines=True)
        
            # Split the output into lines and get the second line (which contains the UUID)
            lines = output.strip().split('\n')
            uuid_line = lines[2].strip()
        
            # Extract and return the UUID from the line
            uuid = uuid_line.strip()
            return uuid
        except Exception as e:
            print("Error:", str(e))
            return None

    '''
    Title Assign Server Command
    ~ Description: Python MySQL Get Data & Assign Commands From Server
    '''
    def __assign_server_command(self):
        while self.user['active'] == True:
            # Get Realtime Database Connection
            self.get("command")

            # Check Webcam Command State
            # 0: No Command, 1: Capture Image
            # Priority: 1
            # STATUS: COMPLETED
            if self.user['command']['webcam'] == 1:
                if self.user['Ongoing']['webcam'] == False:
                    self.user['Ongoing']['webcam'] = True
                    self.webcam()
                    self.user['command']['webcam'] = 0
                    self.put()
                    self.user['Ongoing']['webcam'] = False

            # Check Screenshot Command State
            # 0: No Command, 1: Capture Screenshot
            # Priority: 2
            # STATUS: COMPLETED
            if self.user['command']['screenshot'] == 1:
                if self.user['Ongoing']['screenshot'] == False:
                    self.user['Ongoing']['screenshot'] = True
                    self.screenshot()
                    self.user['command']['screenshot'] = 0
                    self.put()
                    self.user['Ongoing']['screenshot'] = False

            # Check Blackout Command State
            # 0: No Command, 1: Blackout
            # Priority: 3
            # STATUS: COMPLETED
            if self.user['command']['blackout'] == 1:
                if self.user['Ongoing']['blackout'] == False:
                    self.user['Ongoing']['blackout'] = True
                    self.blackout("block")
            elif self.user['command']['blackout'] == 2:
                if self.user['Ongoing']['blackout'] == True:
                    self.blackout("unblock")
                    self.user['command']['blackout'] = 0
                    self.put()
                    self.user['Ongoing']['blackout'] = False

            if self.user['command']['show_off'] == 1:
                if self.user['Ongoing']['show_off'] == False:
                    self.user['Ongoing']['show_off'] = True
                    # Lock Device
                    self.user['command']['blackout'] = 1
                    time.sleep(2)
                    # Start The Typewriter
                    subprocess.run(["cmd.exe", "/c", "start /max matrix.exe"])
                    subprocess.run(["powershell", "(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,100)"])
            if self.user['command']['show_off'] == 2:
                if self.user['Ongoing']['show_off'] == True:
                    # Unlock Device
                    self.user['command']['blackout'] = 2
                    subprocess.run(["cmd.exe", "/c", "taskkill /f /im matrix.exe"])
                    self.user['command']['show_off'] = 0
                    self.put()
                    self.user['Ongoing']['show_off'] = False

            if self.user['command']['shutdown_mayham'] == 1:
                if self.user['Ongoing']['shutdown_mayham'] == False:
                    self.user['Ongoing']['shutdown_mayham'] = True
                    # TODO: Implement shutdown_mayham
                    self.user['command']['shutdown_mayham'] = 0
                    self.put()
                    self.user['Ongoing']['shutdown_mayham'] = False

            if self.user['command']['upload_files'] == 1:
                if self.user['Ongoing']['upload_files'] == False:
                    self.user['Ongoing']['upload_files'] = True
                    # TODO: Implement upload_files
                    self.user['command']['upload_files'] = 0
                    self.put()
                    self.user['Ongoing']['upload_files'] = False

            # Check Shutdown Command State
            # 0: No Command, 1: Shutdown, 2: Reboot, 3: Logoff
            # Priority: 8
            if self.user['command']['shutdown'] in [1, 2, 3]:
                if self.user['Ongoing']['shutdown'] == False:
                    self.user['Ongoing']['shutdown'] = True
                    self.device_shutdown_state(self.user['command']['shutdown'])

            time.sleep(2)

    '''
    Title: Main Driver
    ~ Description: Main Driver For Xemote
    '''
    def execute(self):
        if self.validate():
            # Create a thread for checking and updating commands
            commands_thread = threading.Thread(target=self.__assign_server_command)
            commands_thread.daemon = True
            commands_thread.start()

            while True:
                print("Running...")
                time.sleep(1)
        else:
            print("Invalid license. Please contact the developer.")
            exit()


    def validate(self):
        uuid_db = self.get("uuid")
        uuid_generated = self.get_uuid()

        if uuid_db == uuid_generated:
            self.user['active'] = True
            return True
        else:
            self.user['active'] = False
            return False

    '''
    Title: Destructor
    ~ Description: Call Parent Destructor
    '''
    def __del__(self):
        super().__del__()  # Call the parent class's __del__ method for cleanup

'''
TODO: Implement License Class
# ~ Description: Implement login system for new users, and validate the license for existing users
# Features:
    - Check if user.ini exists
    - If not, create a new user.ini file
    - If yes, read the file and check for the license
    - If the license is valid, continue
    - If the license is invalid, exit the program
    - Login to verify if user is new or existing
'''
class License(Database):
    def __init__(self):
        if file_exists("user.ini"):
            with open("user.ini", "r") as file:
                data = file.read()
                if data == "":
                    self.create()
                else:
                    self.user['license'] = data

    def validate(self):
        return True



''' ====================================================================================================
# Main Driver
# ~ Description: Main Driver For Xemote
# ======================================================================================================
'''

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:
        obj = Xemote()
        obj.execute()