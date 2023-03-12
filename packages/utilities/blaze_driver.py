from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import webdriver_manager
import unittest
from time import sleep
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as OF
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains as AC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as OC
from selenium.webdriver.edge.options import Options as OE
from selenium.webdriver.edge.service import Service
import string
import random


def get_chrome_driver():
    my_driver = webdriver.Chrome()
    return my_driver


def get_firefox_driver():
    my_driver = webdriver.Firefox()
    return my_driver


def get_edge_driver():
    my_driver = webdriver.Edge()
    return my_driver

# def get_firefox_driver():
#     firefox_options = OF()
#     # firefox_options.add_argument('--headless')
#
#     my_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
#     return my_driver
