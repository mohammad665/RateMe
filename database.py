import datetime
from kivy.network.urlrequest import UrlRequest
import certifi
from json import dumps

web_api_key = 'AIzaSyCTIOGEmfhCSnWsCfsDVAa6L41cC3m0iiU'
class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            email, password, name, created = line.strip().split(";")
            self.users[email] = (password, name, created)

        self.file.close()

    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1

    def add_user(self, email, password, name):

        signup_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=" + web_api_key
        signup_payload = dumps(
            {"full_name": name,"email": email, "password": password, "returnSecureToken": "true"})

        UrlRequest(signup_url, req_body=signup_payload,
                on_success=self.successful_login,
                on_failure=self.sign_up_failure,
                on_error=self.sign_up_error, ca_file=certifi.where())

        print(failure_data)
        # if email.strip() not in self.users:
        #     self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
        #     self.save()
        #     return 1
        # else:
        #     print("Email exists already")
        #     return -1
    def successful_login(self, urlrequest, log_in_data):
        """Collects info from Firebase upon successfully registering a new user.
        """
        # self.hide_loading_screen()
        # self.refresh_token = log_in_data['refreshToken']
        # self.localId = log_in_data['localId']
        # self.idToken = log_in_data['idToken']
        # self.save_refresh_token(self.refresh_token)
        # self.login_success = True
        # if self.debug:
        #     print("Successfully logged in a user: ", log_in_data)
        print("i am fucking here")
        return 1

    def sign_up_failure(self, urlrequest, failure_data):
        """Displays an error message to the user if their attempt to log in was
        invalid.
        """
        # self.hide_loading_screen()
        # self.email_exists = False  # Triggers hiding the sign in button
        print(failure_data)
        # msg = failure_data['error']['message'].replace("_", " ").capitalize()
        # # Check if the error msg is the same as the last one
        # if msg == self.sign_up_msg:
        #     # Need to modify it somehow to make the error popup display
        #     msg = " " + msg + " "
        # self.sign_up_msg = msg
        # if msg == "Email exists":
        #     self.email_exists = True
        # if self.debug:
        #     print("Couldn't sign the user up: ", failure_data)

    def sign_up_error(self, *args):
        # self.hide_loading_screen()
        # if self.debug:
        #     print("Sign up Error: ", args)
        pass

    def sign_in_failure(self, urlrequest, failure_data):
        """Displays an error message to the user if their attempt to create an
        account was invalid.
        """
        # self.hide_loading_screen()
        # self.email_not_found = False  # Triggers hiding the sign in button
        print(failure_data)
        # msg = failure_data['error']['message'].replace("_", " ").capitalize()
        # # Check if the error msg is the same as the last one
        # if msg == self.sign_in_msg:
        #     # Need to modify it somehow to make the error popup display
        #     msg = " " + msg + " "
        # self.sign_in_msg = msg
        # if msg == "Email not found":
        #     self.email_not_found = True
        # if self.debug:
        #     print("Couldn't sign the user in: ", failure_data)

    def sign_in_error(self, *args):
        # self.hide_loading_screen()
        # if self.debug:
        #     print("Sign in error", args)
        pass

    def validate(self, email, password):
        
        sign_in_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=" + web_api_key
        sign_in_payload = dumps(
            {"email": email, "password": password, "returnSecureToken": True})

        conn = UrlRequest(sign_in_url, req_body=sign_in_payload,
                   on_success=self.successful_login,
                   on_failure=self.sign_in_failure,
                   on_error=self.sign_in_error, ca_file=certifi.where())
        conn.wait()

        return conn.result
        # if self.get_user(email) != -1:
        #     return self.users[email][0] == password
        # else:
        #     return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]