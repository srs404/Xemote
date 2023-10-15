import mysql.connector

class Xemote:
    # Constructor
    def __init__(self):
        # Database Connection Credentials Dictionary
        self.__db = {
            'server': 'localhost',
            'username': 'root',
            'password': '',
            'database': 'xemote'
        }
        # User Controller Dictionary
        self.__user = {
            'userID': '123456',
            'status': False,
            'command': {
                'shutdown': 0,
                'reboot': 0,
                'logoff': 0,
                'webcam': 0,
                'screenshot': 0,
                'blackout': 0,
                'show_off': 0,
                'shutdown_mayham': 0,
                'upload_files': 0
            },
            'db': {

            }
        }

    # Destructor
    def __del__(self):
        self.__user['db']['connection'].close()
        print("Destructor Initialized!")

    # Get Command From Database
    def get_Data(self):
        try:
            sql = "SELECT shutdown,restart,logoff,webcam,screenshot,blackout,showoff,shutdown_mayham,upload_files FROM command_center WHERE uuid=" + self.__user['userID']
            self.__user['db']['cursor'].execute(sql)
            result = self.__user['db']['cursor'].fetchall()

            i = 0
            for data in self.__user['command']:
                self.__user['command'][data] = result[0][i]
                i = i + 1

            self.__user['status'] = True
        except Exception:
            self.__user['status'] = False

    def operation_center(self):
        if(self.__user['status']):
            print(self.__user['command'])
        else:
            print("No Data")

    # Establish Database Connection
    def connect_DB(self):
        try:
            self.__user['db']['connection'] = mysql.connector.connect(
                host=self.__db['server'],
                user=self.__db['username'],
                password=self.__db['password'],
                database=self.__db['database']
            )
            self.__user['db']['cursor'] = self.__user['db']['connection'].cursor()
        except Exception:
            print("Check Connection To Internet Or Server!")


# Main Driver
obj = Xemote()

obj.connect_DB()
obj.get_Data()
obj.operation_center()
del obj