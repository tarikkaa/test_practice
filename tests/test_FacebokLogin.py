import pytest

from pageObjects.FacebookLoginPage import FacebookLoginPage
from utilities.baseClass import BaseClass


class FacebookTest(BaseClass):


    def test_login(self):
        self.getNewLink("https://www.facebook.com/")
