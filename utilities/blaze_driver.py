from webdriver_manager.chrome import ChromeDriverManager
import unittest
from time import sleep
import HtmlTestRunner
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox import options as O
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains as AC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service


def get_chrome_driver():
    my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return my_driver

def get_firefox_driver():
    my_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    return my_driver
