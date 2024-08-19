import string
from dataclasses import dataclass


@dataclass
class User:
    first_name: str  # min: 2 max: 30 char
    last_name: str  # min: 2 max: 30 char
    email: str  # min: 7 max: 50 char
    password: str  # min: 14 max: 30 char [1 Upper, 1 Number]


class UserValidator:
    @staticmethod
    def check_first_name(user: User) -> bool:
        if user.first_name:
            if 2 <= len(user.first_name) <= 30:
                print('First Name: Passed!')
                return True
            else:
                print('First Name: Failed... [Incorrect First Name Length.]')
                return False
        else:
            print('error: No First Name Provided...')
            return False

    @staticmethod
    def check_last_name(user: User) -> bool:
        if user.last_name:
            if 2 <= len(user.last_name) <= 30:
                print('Last Name: Passed!')
                return True
            else:
                print('Last Name: Failed... [Incorrect Last Name Length.]')
                return False
        else:
            print('error: No Last Name Provided...')
            return False

    @staticmethod
    def check_email(user: User) -> bool:
        if user.email:
            if '@' in user.email:
                if 7 <= len(user.email) <= 50:
                    print('Email: Passed!')
                    return True
                else:
                    print('Email: Failed... [Incorrect Email Length]')
                    return False
            else:
                print('Email: Failed... [Not a valid email]')
                return False
        else:
            print('error: No Email Provided...')
            return False

    @staticmethod
    def check_password(user: User) -> bool:
        if user.password:
            if all([
                len(user.password) >= 14,
                any(c in user.password for c in string.ascii_lowercase),
                any(c in user.password for c in string.ascii_uppercase),
                any(c in user.password for c in string.digits),
            ]):
                print("Password: Passed!")
            else:
                print("Password: Failed... [Password must be minimum length 14, contain a number and an uppercase]")
        else:
            print('error: No Password Provided')
            return False
