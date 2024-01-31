# Class: Database
import mysql.connector
import json

# Class: Arsenal
import subprocess
import cv2
import pyautogui

# Class: Xemote
import time
import platform
import uuid
import threading

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
            'userID': '123456',
            'active': False,
            'command': {
                'shutdown': 3, # 0: No Command, 1: Shutdown, 2: Reboot, 3: Logoff
                'webcam': 0,
                'screenshot': 0,
                'blackout': 0,
                'show_off': 0,
                'shutdown_mayham': 0,
                'upload_files': 0
            },
            'Ongoing': {
                'shutdown': False, # 0: No Command, 1: Shutdown, 2: Reboot, 3: Logoff
                'webcam': False,
                'screenshot': False,
                'blackout': False,
                'show_off': False,
                'shutdown_mayham': False,
                'upload_files': False
            },
            'db': {
            
            }
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
        print("Database connection closed")

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
                # Convert the JSON string to a Python dictionary
                return json.loads(result[0])
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
        self.user['db']['cursor'].close()
        self.user['db']['connection'].close()
        print("Database connection closed")

class Arsenal(Database):
    def __init__(self):
        super().__init__()

    '''
    Title: Webcam
    ~ Description: Capture image from webcam
    Status: Completed
    '''
    def webcam(self, filename="image.jpg"):
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
        if state in ["shutdown", "reboot", "logoff"]:
            self.user['command']['shutdown'] = 0
            super().put()
        if state == 1:
            subprocess.call(["shutdown", "/s"])
        elif state == 2:
            subprocess.call(["shutdown", "/r"])
        elif state == 3:
            subprocess.call(["shutdown", "/l"])
        else:
            print("Invalid command")

    def __del__(self):
        super().__del__()  # Call the parent class's __del__ method for cleanup

class Xemote(Arsenal):
    def __init__(self):
        super().__init__()

    '''
    Title: Get Device UUID
    '''
    def get_system_uuid(self):
        try:
            # Get the system's UUID (Universally Unique Identifier)
            system_uuid = platform.system_alias(platform.system(), platform.release(), platform.version())
            return system_uuid
        except AttributeError:
            print("UUID not available on this system.")
            return None

    def get_uuid(self):
        return str(uuid.uuid4())

    '''
    Title Assign Server Command
    ~ Description: Python MySQL Get Data & Assign Commands From Server
    '''
    def __assign_server_command(self):
        while True:
            # Get Realtime Database Connection
            command_dict = self.get()

            # Check Webcam Command State
            # 0: No Command, 1: Capture Image
            # Priority: 1
            if command_dict['webcam'] == 1:
                if self.user['Ongoing']['webcam'] == False:
                    self.user['Ongoing']['webcam'] = True
                    self.webcam()
                    self.user['command']['webcam'] = 0
                    self.put()
                    self.user['Ongoing']['webcam'] = False

            # Check Screenshot Command State
            # 0: No Command, 1: Capture Screenshot
            # Priority: 2
            if command_dict['screenshot'] == 1:
                if self.user['Ongoing']['screenshot'] == False:
                    self.user['Ongoing']['screenshot'] = True
                    self.screenshot()
                    self.user['command']['screenshot'] = 0
                    self.put()
                    self.user['Ongoing']['screenshot'] = False

            # Check Blackout Command State
            # 0: No Command, 1: Blackout
            # Priority: 3
            if command_dict['blackout'] == 1:
                if self.user['Ongoing']['blackout'] == False:
                    self.user['Ongoing']['blackout'] = True
                    # TODO: Implement blackout
                    self.user['command']['blackout'] = 0
                    self.put()
                    self.user['Ongoing']['blackout'] = False

            if command_dict['show_off'] == 1:
                if self.user['Ongoing']['show_off'] == False:
                    self.user['Ongoing']['show_off'] = True
                    # TODO: Implement show_off
                    self.user['command']['show_off'] = 0
                    self.put()
                    self.user['Ongoing']['show_off'] = False

            if command_dict['shutdown_mayham'] == 1:
                if self.user['Ongoing']['shutdown_mayham'] == False:
                    self.user['Ongoing']['shutdown_mayham'] = True
                    # TODO: Implement shutdown_mayham
                    self.user['command']['shutdown_mayham'] = 0
                    self.put()
                    self.user['Ongoing']['shutdown_mayham'] = False

            if command_dict['upload_files'] == 1:
                if self.user['Ongoing']['upload_files'] == False:
                    self.user['Ongoing']['upload_files'] = True
                    # TODO: Implement upload_files
                    self.user['command']['upload_files'] = 0
                    self.put()
                    self.user['Ongoing']['upload_files'] = False

            # Check Shutdown Command State
            # 0: No Command, 1: Shutdown, 2: Reboot, 3: Logoff
            # Priority: 8
            if command_dict['shutdown'] in [1, 2, 3]:
                if self.user['Ongoing']['shutdown'] == False:
                    self.user['Ongoing']['shutdown'] = True
                    self.user['command']['shutdown'] = 0
                    self.put()
                    super().__del__()
                    print("Shutdown")

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

            # Example: Run a loop to print some messages
            while True:
                print("Main program is running...")
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


    def __del__(self):
        super().__del__()  # Call the parent class's __del__ method for cleanup

# Main Driver
obj = Xemote()

obj.execute()