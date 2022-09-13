import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def VerifylinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, text)))

    def selectOptionbyText(self, locator, text):
        DropDown = Select(locator)
        DropDown.select_by_visible_text(text)

    def getlogger(self):
        loggerName=inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        FileHandler = logging.FileHandler('Logfile.log')  # file handler is the location of parent
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        FileHandler.setFormatter(formatter)
        logger.addHandler(FileHandler)  # another class called file handler need to send object to this class
        logger.setLevel(logging.DEBUG)
        return logger


