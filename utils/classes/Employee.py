import datetime
import random
import string


class Employee:
    def __init__(self, data=None):
        self.email = Employee.create_email()
        self.id = None
        self.id_employment = None
        self.rc = None
        self.data = data

    # SETS
    def set_id(self, ident):
        self.id = ident

    def set_id_employment(self, ident):
        self.id_employment = ident

    def set_rc(self, rc):
        self.rc = rc

    def set_data(self, data):
        self.data = data

    # GETS
    def get_id(self):
        return self.id

    def get_id_employment(self):
        return self.id_employment

    def get_rc(self):
        return self.rc

    def get_email(self):
        return self.email

    def get_employee(self):
        return self.data['employee']

    def get_user(self):
        return self.data['user']

    def get_inquiry(self):
        return self.data['inquiry']

    def get_employment(self):
        return self.data['employment']

    def get_attendance(self):
        return self.data['attendance']

    def get_data(self):
        return self.data

    # OTHERS
    @staticmethod
    def create_email():
        random_string = ''.join(random.sample(string.ascii_lowercase, 4))
        return datetime.datetime.today().strftime('%Y%m%d_%H%M%S') + "_" + random_string + '.test@cognevo.eu'
