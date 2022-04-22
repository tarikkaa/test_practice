#import getpass
import os
import dotenv
from dotenv import load_dotenv

class TestData:
    __find_env = dotenv.find_dotenv(".\\utilities\\test_data\\data.env")
    load_dotenv(__find_env)
    login = os.environ.get("login")
    password = os.environ.get("password")

    #login = input("Login: ")
    #password = getpass.getpass()

    wrong_login = "test@test.com"
    wrong_password = "12345"
    userName = "John Lucky"
    loginPageTitle = "Facebook - log in or sign up"
    mainPageTitle = "(1) Facebook"

